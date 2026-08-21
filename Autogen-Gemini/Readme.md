# 🤖 AutoGen + Google Gemini Integration

A simple Python project demonstrating how to integrate **Microsoft AutoGen** with **Google Gemini** using Google's OpenAI-compatible API endpoint.

This project uses AutoGen's `OpenAIChatCompletionClient` to send a user prompt to the Gemini model and receive an AI-generated response.

---

## 🚀 Project Overview

The purpose of this project is to demonstrate the basic integration between:

```text
Python
   ↓
Microsoft AutoGen
   ↓
OpenAIChatCompletionClient
   ↓
Google Gemini API
   ↓
AI Response
```

The project provides a simple foundation for building more advanced **Agentic AI and Multi-Agent Systems** using AutoGen and Gemini.

---

# ✨ Features

* 🤖 Microsoft AutoGen integration
* 🧠 Google Gemini model integration
* 🔗 OpenAI-compatible Gemini API endpoint
* 🔐 Secure API key management using `.env`
* ⚡ Asynchronous Python execution
* 💬 Natural-language prompt processing
* 🛠️ AutoGen model capability configuration
* 📦 Simple and easy-to-understand project structure

---

# 🛠️ Technologies Used

| Technology                    | Purpose                         |
| ----------------------------- | ------------------------------- |
| 🐍 Python                     | Programming language            |
| 🤖 Microsoft AutoGen          | Agentic AI framework            |
| 🧠 Google Gemini              | Large Language Model            |
| 🔗 OpenAIChatCompletionClient | Model client                    |
| 🔐 python-dotenv              | Environment variable management |
| ⚡ asyncio                     | Asynchronous execution          |

---

# 📂 Project Structure

```text
autogen-gemini-integration/
│
├── 📄 ag-gemini.py
├── 📄 requirements.txt
├── 📄 .env.example
├── 📄 .gitignore
└── 📄 README.md
```

### File Description

| File               | Description                                              |
| ------------------ | -------------------------------------------------------- |
| `ag-gemini.py`     | Main Python program                                      |
| `requirements.txt` | Required Python packages                                 |
| `.env.example`     | Example environment configuration                        |
| `.gitignore`       | Prevents sensitive/unnecessary files from being uploaded |
| `README.md`        | Project documentation                                    |

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/autogen-gemini-integration.git
```

Navigate to the project:

```bash
cd autogen-gemini-integration
```

---

## 2. Create a Virtual Environment

For Windows:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\activate
```

You should see:

```text
(venv)
```

in your terminal.

---

## 3. Install Dependencies

Install the required packages:

```powershell
python -m pip install -r requirements.txt
```

The project uses:

```text
autogen-agentchat
autogen-ext[openai,azure]
python-dotenv
```

---

# 🔑 API Configuration

This project requires a **Google Gemini API key**.

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

The application loads the environment variables using:

```python
from dotenv import load_dotenv

load_dotenv()
```

The API key is then retrieved using:

```python
gemini_key = os.getenv("GEMINI_API_KEY")
```

---

## 🔐 Security

**Never upload your `.env` file to GitHub.**

Your `.gitignore` should contain:

```gitignore
venv/
.venv/
env/

.env
.env.*
!.env.example

__pycache__/
*.py[cod]

.vscode/
.idea/

.DS_Store
Thumbs.db
```

Instead, upload `.env.example`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

This keeps your API key private.

---

# 🧠 AutoGen + Gemini Configuration

The project uses:

```python
from autogen_core.models import UserMessage, ModelInfo
from autogen_ext.models.openai import OpenAIChatCompletionClient
```

Gemini model capabilities are explicitly defined:

```python
gemini_model_info = ModelInfo(
    vision=True,
    function_calling=True,
    json_output=True,
    structured_output=True,
    family="gemini",
)
```

The Gemini model client is then created:

```python
model_client = OpenAIChatCompletionClient(
    model="gemini-3-flash-preview",
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    model_info=gemini_model_info,
)
```

---

# 🔄 How It Works

### 1️⃣ Load API Key

The program loads the Gemini API key from `.env`.

```python
load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
```

---

### 2️⃣ Configure Model Information

AutoGen requires information about the capabilities supported by the model.

```python
ModelInfo(
    vision=True,
    function_calling=True,
    json_output=True,
    structured_output=True,
    family="gemini",
)
```

---

### 3️⃣ Create Gemini Client

The project uses AutoGen's OpenAI-compatible model client:

```python
OpenAIChatCompletionClient
```

with Google's OpenAI-compatible endpoint.

---

### 4️⃣ Send User Message

The application sends a question to Gemini:

```python
UserMessage(
    content="What is the AutoGen framework in Agentic AI?",
    source="user"
)
```

---

### 5️⃣ Receive AI Response

AutoGen sends the request to Gemini and receives the generated response:

```python
response = await model_client.create([
    UserMessage(
        content="What is the AutoGen framework in Agentic AI?",
        source="user"
    )
])
```

---

### 6️⃣ Display the Result

The response is printed in the terminal:

```python
print("Response:\n", response.content)
```

---

# ▶️ Running the Project

After activating your virtual environment and configuring `.env`, run:

```powershell
python ag-gemini.py
```

You should see:

```text
Response:

AutoGen is an open-source framework developed by Microsoft
designed to simplify the creation, orchestration, and automation
of Multi-Agent Systems...
```

The exact response will be generated dynamically by Gemini.

---

# 💬 Example Prompt

The current project uses:

```text
What is the autogen framework in Agentic AI?
```

You can modify the prompt to ask other questions.

For example:

```text
What is Agentic AI?
```

or:

```text
Explain how multi-agent systems work.
```

or:

```text
What are the main features of Microsoft AutoGen?
```

---

# 🎯 Learning Objectives

This project helps demonstrate practical knowledge of:

* Microsoft AutoGen
* Agentic AI fundamentals
* Large Language Models
* Google Gemini API
* OpenAI-compatible APIs
* Async Python programming
* Environment variable management
* API integration
* AutoGen model clients
* Model capability configuration

---

# 🔮 Future Enhancements

This basic integration can be extended into more advanced Agentic AI applications.

Possible improvements include:

* 🤖 Multiple collaborating agents
* 🔍 Web search agent
* 💻 Coding agent
* 📊 Data analysis agent
* 📝 Research agent
* 👨‍💻 Code review agent
* 🧠 Planner and executor agents
* 🛠️ Custom tool calling
* 👤 Human-in-the-loop workflows
* 🖥️ Streamlit interface
* 💾 Conversation memory
* 🔄 Multi-agent workflows

---

# 📚 Resources

* Microsoft AutoGen documentation
* Google Gemini API documentation
* Python documentation

---

# 👩‍💻 Author

## Ankita Shendge

**B.Tech — Artificial Intelligence & Data Science**

### Areas of Interest

* Artificial Intelligence
* Machine Learning
* Generative AI
* Agentic AI
* Data Science
* Multimodal AI

---

# ⭐ Project Highlights

```text
🐍 Python
   +
🤖 Microsoft AutoGen
   +
🧠 Google Gemini
   +
🔗 OpenAI-Compatible API
   +
⚡ Async Programming
```

A practical demonstration of integrating **Microsoft AutoGen with Google Gemini** as a foundation for building advanced **Agentic AI and Multi-Agent Systems**.

---

# 📜 License

This project is created for **educational, learning, and portfolio purposes**.

Feel free to explore, modify, and extend the project.
