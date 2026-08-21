# 🖼️ Multimodal AI Image Analyzer using AutoGen & Gemini

An interactive **Multimodal AI Image Analyzer** built using **Python, Microsoft AutoGen, Google Gemini, and Streamlit**.

The application allows users to upload an image or use a random sample image, enter a natural-language prompt, and receive an AI-powered analysis of the image.

---

## 🚀 Project Overview

This project demonstrates how **Microsoft AutoGen** can be integrated with **Google Gemini's multimodal capabilities** to build an interactive AI image-analysis application.

The application accepts:

**Image + Natural Language Prompt**

and sends both to the Gemini multimodal model through AutoGen to generate an intelligent response.

### ✨ Key Features

* 🖼️ Upload JPG, JPEG, PNG, and WEBP images
* 🌐 Fetch random sample images
* 👀 Preview selected images
* 💬 Enter custom prompts
* 🤖 Analyze images using Google Gemini
* 🔗 Integrate Microsoft AutoGen
* 🖥️ Interactive Streamlit interface
* 🔐 Secure API key management using `.env`
* ⚡ Asynchronous model execution

---

# 🛠️ Technologies Used

| Technology           | Purpose                         |
| -------------------- | ------------------------------- |
| 🐍 Python            | Core programming language       |
| 🎨 Streamlit         | Web application interface       |
| 🤖 Microsoft AutoGen | AI model integration            |
| 🧠 Google Gemini     | Multimodal image analysis       |
| 🖼️ Pillow           | Image processing                |
| 🌐 Requests          | Fetching sample images          |
| 🔐 python-dotenv     | Environment variable management |
| ⚡ asyncio            | Asynchronous execution          |

---

# 🏗️ Architecture

```text
                    👤 User
                      │
                      ▼
             ┌──────────────────┐
             │   Streamlit UI   │
             └────────┬─────────┘
                      │
               Image + Prompt
                      │
                      ▼
             ┌──────────────────┐
             │ Microsoft AutoGen│
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ AutoGen Model    │
             │     Client       │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │  Google Gemini   │
             │ Multimodal Model │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │  AI Analysis     │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Streamlit Result │
             └──────────────────┘
```

---

# 📂 Project Structure

```text
Autogen-Multiagent/
│
├── 📁 Images/
│   ├── 🖼️ Home.png
│   ├── 🖼️ Output1.png
│   └── 🖼️ Output2.png
│
├── 📄 ag-multiagent.py
├── 📄 requirements.txt
├── 📄 .gitignore
├── 📄 .env.example
└── 📄 README.md
```

### File Description

| File / Folder      | Description                       |
| ------------------ | --------------------------------- |
| `Images/`          | Contains application screenshots  |
| `Home.png`         | Home page screenshot              |
| `Output1.png`      | First AI analysis output          |
| `Output2.png`      | Second AI analysis output         |
| `ag-multiagent.py` | Main Streamlit application        |
| `requirements.txt` | Python dependencies               |
| `.gitignore`       | Files excluded from Git           |
| `.env.example`     | Example environment configuration |
| `README.md`        | Project documentation             |

---

# 📸 Application Screenshots

The following screenshots demonstrate the application's interface and AI-generated results.

<table>
  <tr>
    <td align="center">
      <img src="./Images/Home.png" alt="Home Page" width="450">
    </td>
    <td align="center">
      <img src="./Images/Output1.png" alt="Output 1" width="450">
    </td>
  </tr>
  <tr>
    <td align="center"><b>🏠 Home Page</b></td>
    <td align="center"><b>📋 Output 1</b></td>
  </tr>

  <tr>
    <td align="center">
      <img src="./Images/Output2.png" alt="Output 2" width="450">
    </td>
    <td></td>
  </tr>
  <tr>
    <td align="center"><b>📋 Output 2</b></td>
    <td></td>
  </tr>
</table>

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/shendgeankita522-blip/autogen-ai-project.git
```

Navigate to the project folder:

```bash
cd autogen-ai-project/Autogen-Multiagent
```

---

## 2. Create a Virtual Environment

For Windows:

```powershell
python -m venv venv
```

Activate the environment:

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

Install all required packages:

```powershell
python -m pip install -r requirements.txt
```

The main dependencies include:

```text
streamlit
python-dotenv
pillow
requests
autogen-core
autogen-agentchat
autogen-ext[openai]
```

---

# 🔑 API Configuration

This project requires a **Google Gemini API key**.

Create a `.env` file inside the `Autogen-Multiagent` directory:

```text
GEMINI_API_KEY=your_actual_gemini_api_key
```

The application loads the environment variable using:

```python
from dotenv import load_dotenv

load_dotenv()
```

and retrieves the API key using:

```python
gemini_key = os.getenv("GEMINI_API_KEY")
```

---

## 🔐 Security

**Never upload your `.env` file to GitHub.**

Your `.gitignore` contains:

```gitignore
venv/
.venv/
.env
.env.*
!.env.example
__pycache__/
*.py[cod]
.streamlit/secrets.toml
```

Instead, the repository contains `.env.example`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

This allows other developers to know which environment variable is required without exposing your private API key.

---

# ▶️ Running the Application

After activating your virtual environment and configuring your API key, run:

```powershell
python -m streamlit run ag-multiagent.py
```

Streamlit will launch the application in your web browser.

---

# 🔄 How the Application Works

### 1️⃣ Choose an Image

The user can select:

* **Upload Image**
* **Use Sample Random Image**

Supported image formats:

```text
JPG
JPEG
PNG
WEBP
```

---

### 2️⃣ Preview the Image

The selected image is displayed in the Streamlit application.

---

### 3️⃣ Enter a Prompt

The user enters a question or instruction about the image.

Example:

```text
Can you describe the content of this image in detail and list its key elements?
```

---

### 4️⃣ Convert Image for AutoGen

The PIL image is converted into an AutoGen image object:

```python
ag_img = AGImage(image)
```

---

### 5️⃣ Create Multimodal Message

The prompt and image are combined into a `UserMessage`:

```python
user_msg = UserMessage(
    content=[prompt, ag_img],
    source="user"
)
```

---

### 6️⃣ Send Request to Gemini

AutoGen communicates with the Gemini model using:

```python
OpenAIChatCompletionClient
```

The application uses Google's OpenAI-compatible API endpoint.

---

### 7️⃣ Display AI Response

The Gemini-generated analysis is returned and displayed in the Streamlit interface.

---

# 💬 Example Prompts

### 📝 Image Description

```text
Describe this image in detail.
```

### 🔍 Object Identification

```text
Identify the main objects visible in this image.
```

### 🌆 Scene Understanding

```text
Explain what is happening in this image.
```

### 📄 Text Extraction

```text
Extract all visible text from this image.
```

### 🎨 Detailed Visual Analysis

```text
Describe the objects, environment, colors, people,
and important visual elements in this image.
```

---

# 🧠 AutoGen + Gemini Integration

The project uses:

```python
from autogen_core import Image as AGImage
from autogen_core.models import ModelInfo, UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
```

The Gemini model client is configured with:

```python
model_client = OpenAIChatCompletionClient(
    model="gemini-3-flash-preview",
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    model_info=gemini_model_info
)
```

The application specifies multimodal model capabilities such as:

```python
ModelInfo(
    vision=True,
    function_calling=True,
    json_output=True,
    family="unknown"
)
```

This enables the AutoGen model client to handle the multimodal request.

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Microsoft AutoGen
* Multimodal Generative AI
* Google Gemini
* Vision-enabled AI models
* OpenAI-compatible APIs
* Python asynchronous programming
* Streamlit application development
* Image processing using Pillow
* Environment variable management
* API integration
* Prompt engineering
* Multimodal AI workflows

---

# 💡 Potential Use Cases

The application can be extended for:

* 🖼️ Image description
* 🔍 Visual question answering
* 📄 Document analysis
* 🧾 Invoice analysis
* 📝 OCR and text extraction
* 🏞️ Scene understanding
* 🛍️ Product image analysis
* 🎓 Educational image analysis
* 🤖 Multimodal AI assistants

---

# 🔮 Future Enhancements

Possible improvements include:

* 🤖 Multiple specialized AutoGen agents
* 🔍 Object detection
* 📝 OCR integration
* 📄 Advanced document analysis
* 🧾 Invoice and receipt processing
* 💾 Analysis history
* 📥 Downloadable analysis reports
* 🗣️ Voice-based image queries
* 📊 Image classification
* 🧠 Specialized vision agents
* 🌐 Deployment using Streamlit Cloud

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
🖼️ Multimodal AI
   +
🎨 Streamlit
```

A practical implementation of an **AI-powered multimodal image analysis application** using modern Generative AI technologies.

---

# 📜 License

This project is created for **educational, learning, and portfolio purposes**.

Feel free to explore, modify, and extend the project.
