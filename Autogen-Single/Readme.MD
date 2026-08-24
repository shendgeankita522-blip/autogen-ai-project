
---

## 📌 Project Overview

The application creates a single AI agent called:

**🌱 NonTech_Mentor**

The agent is designed to explain technical concepts in a simple and understandable way.

Instead of using complicated programming terminology, the mentor:

- Uses simple language
- Avoids unnecessary technical jargon
- Uses real-world examples
- Uses analogies
- Explains concepts step-by-step

---

## 🤖 AI Agent

### 🌱 NonTech_Mentor

The agent has the following role:

> You are a friendly technical educator explaining concepts to a non-technical audience. Avoid code or heavy jargon. Use clear real-world analogies.

The user enters a technical question, and the agent generates an easy-to-understand explanation.

---

## 💡 Example Question

```text
Can you explain how a database index works using a library analogy?
```

The AI mentor explains the concept using a familiar real-world example instead of complicated technical terminology.

---

## ✨ Features

- 🤖 Single AI Agent
- 🌱 Non-Technical Mentor
- 🧠 Google Gemini integration
- 🔗 Microsoft AutoGen
- 🎨 Streamlit web interface
- 🔐 Environment variable support
- 💬 Interactive question input
- ⚡ Asynchronous execution
- 📚 Real-world analogies
- 🚫 Avoids unnecessary technical jargon

---

# 🧠 Architecture

```text
                    👤 User
                      │
                      ▼
              🎨 Streamlit UI
                      │
                      ▼
              🌱 NonTech_Mentor
                      │
                      ▼
               🧠 Google Gemini
                      │
                      ▼
              📖 Simple Explanation
                      │
                      ▼
                    👤 User
```

---

# 🔄 Workflow

```text
1. User opens the Streamlit application
                ↓
2. Gemini API key is loaded
                ↓
3. User enters a question
                ↓
4. NonTech_Mentor receives the question
                ↓
5. AutoGen sends the request to Gemini
                ↓
6. Gemini generates the explanation
                ↓
7. The mentor simplifies the response
                ↓
8. Explanation is displayed in Streamlit
```

---

# 🛠️ Technologies Used

- Python
- Microsoft AutoGen
- AutoGen AgentChat
- Google Gemini
- Streamlit
- python-dotenv
- asyncio

---

# 📂 Project Structure

```text
autogen-single-agent-mentor/
│
├── 📁 Images/
│   ├── 🖼️ Output1.png
│
├── 📄 ag-single-agent.py
├── 📄 requirements.txt
├── 📄 .gitignore
├── 📄 .env.example
└── 📄 README.md
```

---

# 📸 Application Screenshots

The following screenshots show the application running in Streamlit.

## 🖼️ Output 1

<p align="center">
  <img src="./Images/Output1.png" alt="Single Agent Mentor Output 1" width="900">
</p>

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/autogen-single-agent-mentor.git
```

Go to the project folder:

```bash
cd autogen-single-agent-mentor
```

---

## 2. Create Virtual Environment

For Windows:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\activate
```

After activation, you should see:

```text
(venv)
```

---

# 📦 Install Dependencies

Run:

```powershell
python -m pip install -r requirements.txt
```

---

# 📄 requirements.txt

Create a file called:

```text
requirements.txt
```

Add:

```text
streamlit
python-dotenv
autogen-agentchat
autogen-ext[openai,azure]
```

---

# 🔑 Gemini API Key

This project requires a Google Gemini API key.

Create a file named:

```text
.env
```

Add:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
```

The application loads the API key using:

```python
from dotenv import load_dotenv

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
```

---

# 🔐 .env.example

For GitHub, create:

```text
.env.example
```

Add:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### ⚠️ Important

Never upload your actual `.env` file to GitHub.

Your `.env` file contains your private API key.

---

# 🚫 .gitignore

Create a file named:

```text
.gitignore
```

Add:

```gitignore
# Virtual Environment
venv/
.venv/
env/

# Environment Variables
.env
.env.*
!.env.example

# Python Cache
__pycache__/
*.py[cod]
*$py.class

# Streamlit
.streamlit/secrets.toml

# VS Code
.vscode/

# PyCharm
.idea/

# Jupyter
.ipynb_checkpoints/

# Logs
*.log

# Temporary Files
*.tmp
*.temp

# Operating System
.DS_Store
Thumbs.db
```

---

# ▶️ How to Run

Activate your virtual environment:

```powershell
.\venv\Scripts\activate
```

Then run the Streamlit application:

```powershell
python -m streamlit run ag-single-agent.py
```

The application will start at:

```text
http://localhost:8501
```

Open the URL in your browser.

---

# 🖥️ Using the Application

### Step 1

Open the application in your browser.

### Step 2

Provide your Gemini API key.

You can either:

- Store it in `.env`
- Enter it through the Streamlit sidebar

### Step 3

Enter your question.

Example:

```text
Can you explain how a database index works using a library analogy?
```

### Step 4

Click:

```text
🚀 Ask Mentor
```

### Step 5

The AI mentor generates a simple explanation.

---

# 🧩 AutoGen Components

The project uses the AutoGen AgentChat framework.

```python
from autogen_agentchat.agents import AssistantAgent
```

`AssistantAgent` provides the main AI agent used in this application. :contentReference[oaicite:1]{index=1}

The project also uses:

```python
from autogen_ext.models.openai import OpenAIChatCompletionClient
```

This model client is used to communicate with the configured OpenAI-compatible model endpoint. :contentReference[oaicite:2]{index=2}

---

# 🧠 Model Configuration

The project connects Gemini through the OpenAI-compatible endpoint:

```text
https://generativelanguage.googleapis.com/v1beta/openai/
```

The configured model is:

```text
gemini-3-flash-preview
```

---

# 🎯 Learning Objectives

This project demonstrates:

- Agentic AI fundamentals
- Single-agent architecture
- Microsoft AutoGen
- AutoGen AgentChat
- Google Gemini integration
- LLM integration
- Prompt engineering
- Async Python
- Streamlit application development
- Environment variable management
- AI-based educational assistants

---

# 🌍 Real-World Applications

This type of AI mentor can be used for:

### 🎓 Education

Explain difficult concepts to students.

### 👨‍💻 Technical Training

Help beginners understand programming concepts.

### 🏢 Employee Training

Explain technical systems to non-technical employees.

### 📚 Learning Assistant

Convert complex topics into simple explanations.

### 💬 Customer Support

Explain technical products and services in simple language.

---

# 🔮 Future Enhancements

Future versions could include:

- 💬 Chat history
- 🎙️ Voice input
- 🔊 Text-to-speech
- 🌐 Web search
- 📚 PDF learning material
- 🧠 Long-term memory
- 🌍 Multiple languages
- 📊 Learning progress tracking
- 🎓 Personalized learning paths
- 🤖 Multiple specialized agents

---

# 📊 Project Highlights

```text
🐍 Python
   +
🤖 Microsoft AutoGen
   +
🧠 Google Gemini
   +
🌱 Single AI Agent
   +
🎨 Streamlit
   +
⚡ Async Programming
   +
📚 Educational AI
```

---

# 👩‍💻 Author

## Ankita Shendge

**B.Tech in Artificial Intelligence & Data Science**

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Generative AI
- Agentic AI
- Data Science
- Multi-Agent Systems
- Large Language Models

---

# 📜 License

This project is created for educational, learning, and portfolio purposes.

Feel free to explore, modify, and extend the project.

---

# ⭐ Support

If you find this project useful, consider giving the GitHub repository a ⭐ star.

Thank you for checking out the project! 🚀
