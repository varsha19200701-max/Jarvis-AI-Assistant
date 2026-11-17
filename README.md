# 🤖 JARVIS AI Assistant — Chat + Voice

An AI-powered virtual assistant built using Python that allows users to interact through text and voice.

## 🚀 Live Demo

### 🌐 [CLICK HERE TO OPEN JARVIS AI ASSISTANT](https://jarvis-ai-assistant-lhr4.onrender.com/)

**Deployed Application:** Render

Try the live application and interact with JARVIS through its Chat Assistant and Voice Assistant.

---

## 📌 Project Overview

JARVIS AI Assistant is a **General-Purpose Conversational AI Assistant** designed to provide intelligent, interactive, and context-aware responses through both text and voice.

It uses a Large Language Model (LLM) to understand user queries, process conversational context, and generate relevant AI-powered responses.

The application provides two ways to interact:

- **Web Chat:** Type a message and receive an AI-generated response.
- **Web Voice Assistant:** Record a message using your browser microphone. JARVIS transcribes it, generates an answer, and plays a spoken reply.
- **Conversation Context:** Recent messages are sent along so JARVIS can follow the conversation and provide context-aware responses.

### 🧠 What Can JARVIS Help With?

JARVIS is designed to assist users with a variety of general-purpose queries, including:

- **General Knowledge:** Questions about everyday topics, science, technology, and other subjects.
- **Educational Assistance:** Understanding academic concepts and getting explanations of difficult topics.
- **Programming Assistance:** Learning programming concepts, understanding code, and getting help with coding-related questions.
- **Information and Explanations:** Getting explanations, summaries, and information on different subjects.
- **Conversational Interaction:** Having natural conversations while maintaining recent conversation context.

The quality and scope of responses depend on the underlying AI model.

> JARVIS is a conversational AI assistant. It does not control your computer or perform autonomous background tasks.

## 🤖 Large Language Model (LLM) Used

**JARVIS is powered by OpenAI GPT-OSS 20B, accessed through the Groq API.**

GPT-OSS 20B is an open-weight Large Language Model (LLM) that processes user queries and generates conversational AI responses.

### LLM Configuration

| Component | Technology |
|---|---|
| **LLM Model** | **OpenAI GPT-OSS 20B (`openai/gpt-oss-20b`)** |
| AI Inference Provider | Groq API |
| Voice Transcription Model | Groq Whisper (`whisper-large-v3-turbo`) |
| Text-to-Speech | gTTS |
| Interface | Gradio |

### How the AI Components Work Together

1. The user submits a question through text or voice.
2. If voice input is used, Groq Whisper converts the recorded speech into text.
3. The user's message and recent conversation history are sent to GPT-OSS 20B through the Groq API.
4. The LLM processes the query and generates an appropriate response.
5. If voice interaction is used, gTTS converts the generated response into spoken audio.
6. The response is displayed or played in the browser.

## ✨ Key Features

1. AI-powered text conversations.
2. Voice-based interaction through a browser microphone.
3. Speech-to-text conversion.
4. Text-to-speech responses.
5. Conversation history and contextual responses.
6. Browser-based interface using Gradio.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Gradio | Browser-based chat and voice interface |
| OpenAI GPT-OSS 20B | Large Language Model used to generate AI responses |
| Groq API | Provides access to the LLM for AI inference |
| Groq Whisper | Converts recorded speech into text |
| gTTS | Generates spoken audio replies |
| python-dotenv | Loads environment variables |

## 📂 Project Structure

| File | Purpose |
|---|---|
| `app.py` | Web interface, chat functionality, voice transcription and audio responses |
| `main.py` | Original terminal-based assistant |
| `requirements.txt` | Dependencies for the hosted web application |
| `requirements-local.txt` | Dependencies for the original terminal version |
| `.env.example` | Example environment configuration |
| `.gitignore` | Excludes private and unnecessary local files |
| `README.md` | Project documentation |

## ⚙️ Run the Web Application Locally

**Requirements:** Python 3.10 or newer.

### 1. Clone the repository

```bash
git clone https://github.com/varsha19200701-max/Jarvis-AI-Assistant.git
```

### 2. Open the project folder

```bash
cd Jarvis-AI-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows Command Prompt:

```bat
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Configure the API key

Create a `.env` file in the project folder and add:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-20b
```

Replace the placeholder with your actual Groq API key.

### 7. Run the application

```bash
python app.py
```

Open the local address printed in the terminal, usually:

`http://127.0.0.1:7860`

## 🎤 Run the Original Terminal Version

The original `main.py` supports local microphone and speaker interaction.

Install its separate dependencies:

```bash
pip install -r requirements-local.txt
```

Run:

```bash
python main.py
```

Choose:

- `1` — Voice Assistant
- `2` — Chat Assistant
- `3` — Exit

## ☁️ Deployment

The web application is deployed using **Render**.

Deployment configuration:

- **Platform:** Render
- **Runtime:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app.py`

The Groq API key is securely configured through Render Environment Variables.

## 🔄 How the Web Application Works

1. Gradio displays the chat and microphone controls in the browser.
2. Typed messages are sent to the AI response function.
3. Voice recordings are sent to Groq's Whisper transcription API.
4. The recognized words are sent to the same AI response function.
5. GPT-OSS 20B generates an AI response through the Groq API.
6. gTTS converts the response into an MP3 audio file.
7. The browser plays JARVIS's spoken response.

## 🔐 Security Notes

- Never upload your actual `.env` file to GitHub.
- Never expose your Groq API key in public files.
- Store deployment API keys using Render Environment Variables.
- Keep `.env` and `.venv` excluded through `.gitignore`.

## 👩‍💻 Source Code

**GitHub Repository:**  
https://github.com/varsha19200701-max/Jarvis-AI-Assistant

**Live Application:**  
https://jarvis-ai-assistant-lhr4.onrender.com/