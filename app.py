"""
JARVIS Web Assistant
A Gradio web interface for text chat and voice conversation.
The Groq API key is read from the hosting platform's Secrets or local .env file.
"""

import os
import tempfile
from pathlib import Path

import gradio as gr
from dotenv import load_dotenv
from groq import Groq
from gtts import gTTS

load_dotenv()

MODEL_NAME = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")
TRANSCRIPTION_MODEL = os.getenv("GROQ_TRANSCRIPTION_MODEL", "whisper-large-v3-turbo")
SYSTEM_MESSAGE = (
    "You are JARVIS, a friendly and helpful virtual AI assistant. "
    "Explain things clearly and use simple language."
)


def get_client():
    """Create a Groq client using the private environment variable."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise gr.Error(
            "Groq API key is not configured. The Space owner must add "
            "GROQ_API_KEY under Settings > Secrets."
        )
    return Groq(api_key=api_key)


def get_ai_reply(message, history):
    """Send the user's message and previous chat turns to Groq."""
    client = get_client()
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}]

    # Keep the recent conversation context, not the entire session forever.
    for item in (history or [])[-12:]:
        if isinstance(item, dict) and item.get("role") in {"user", "assistant"}:
            content = item.get("content")
            if isinstance(content, str):
                messages.append({"role": item["role"], "content": content})

    messages.append({"role": "user", "content": message})
    try:
        result = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
        )
        return result.choices[0].message.content or "I couldn't create a response."
    except Exception as exc:
        raise gr.Error(f"Groq could not generate a response: {exc}") from exc


def chat_reply(message, history):
    """Handle typed chat messages."""
    if not message or not message.strip():
        return "", history
    answer = get_ai_reply(message.strip(), history)
    updated = (history or []) + [
        {"role": "user", "content": message.strip()},
        {"role": "assistant", "content": answer},
    ]
    return "", updated


def transcribe_audio(audio_path):
    """Transcribe a microphone recording using Groq's audio transcription API."""
    if not audio_path:
        raise gr.Error("Please record a voice message first.")
    client = get_client()
    try:
        with open(audio_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=(Path(audio_path).name, audio_file.read()),
                model=TRANSCRIPTION_MODEL,
                response_format="text",
            )
        # Groq SDK may return plain text or a response object depending on version.
        if isinstance(transcription, str):
            return transcription.strip()
        return getattr(transcription, "text", str(transcription)).strip()
    except Exception as exc:
        raise gr.Error(f"Could not transcribe your recording: {exc}") from exc


def make_speech_file(text):
    """Create an MP3 that the browser can play."""
    output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
    try:
        gTTS(text=text, lang="en").save(output_path)
        return output_path
    except Exception:
        try:
            os.remove(output_path)
        except OSError:
            pass
        raise


def voice_reply(audio_path, history):
    """Transcribe a recording, ask Groq, and return both text and spoken audio."""
    transcript = transcribe_audio(audio_path)
    if not transcript:
        raise gr.Error("I couldn't detect any speech. Please try recording again.")

    answer = get_ai_reply(transcript, history)
    updated = (history or []) + [
        {"role": "user", "content": transcript},
        {"role": "assistant", "content": answer},
    ]
    speech_path = make_speech_file(answer)
    return updated, None, speech_path


def clear_chat():
    return [], None, None


with gr.Blocks(title="JARVIS AI Assistant") as demo:
    gr.Markdown(
        """
        # 🤖 JARVIS AI Assistant
        Chat with JARVIS by typing or recording a voice message.
        """
    )
    gr.Markdown(
        "**How to use:** Type a message in Chat, or record your voice in Voice Assistant. "
        "The voice feature transcribes your recording and plays JARVIS's spoken reply."
    )

    chatbot = gr.Chatbot(label="Conversation", height=420)
    with gr.Tab("Chat"):
        with gr.Row():
            text_input = gr.Textbox(
                label="Your message",
                placeholder="Ask JARVIS anything...",
                scale=8,
                lines=2,
            )
            send_button = gr.Button("Send", variant="primary", scale=1)
        gr.Markdown("Press Enter or click Send.")
    with gr.Tab("Voice Assistant"):
        microphone = gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="Record your message",
        )
        voice_button = gr.Button("Send voice message", variant="primary")
        voice_output = gr.Audio(label="JARVIS speaking", type="filepath", autoplay=True)

    clear_button = gr.Button("Clear conversation")

    send_button.click(
        chat_reply, inputs=[text_input, chatbot], outputs=[text_input, chatbot]
    )
    text_input.submit(
        chat_reply, inputs=[text_input, chatbot], outputs=[text_input, chatbot]
    )
    voice_button.click(
        voice_reply,
        inputs=[microphone, chatbot],
        outputs=[chatbot, microphone, voice_output],
    )
    clear_button.click(
        clear_chat, outputs=[chatbot, microphone, voice_output]
    )

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft())
