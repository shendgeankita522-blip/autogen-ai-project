

A Multi-Agent AI application built using **Microsoft AutoGen, Google Gemini, Python, and Streamlit**.

This project demonstrates how multiple specialized AI agents can communicate and collaborate to create a coordinated morning schedule while ensuring that all deadlines are met.

---

## 📌 Project Overview

It is **7:30 AM at home**.

The father has three responsibilities:

- 👦 Kid 1 needs to go to **School A** and arrive by **8:00 AM**
- 👧 Kid 2 needs to go to **School B** and arrive by **8:15 AM**
- 👨 Father needs to go to **Office** and arrive by **9:00 AM**

The application uses three specialized AI agents to create a coordinated plan.

---

## 👥 Multi-Agent System

### 👦 School Agent 1

Responsible for taking **Kid 1 to School A**.

**Deadline:** 8:00 AM

### 👧 School Agent 2

Responsible for taking **Kid 2 to School B**.

**Deadline:** 8:15 AM

### 👨 Office Agent

Responsible for taking **Father to Office**.

**Deadline:** 9:00 AM

The Office Agent reviews the plans created by both school agents and coordinates the complete schedule.

---

📸 Application Screenshots

The screenshots below show the actual Streamlit application outputs.

🖼️ Output 1
<p align="center"> <img src="./Images/Output1.png" alt="AutoGen Multi-Agent Morning Coordinator - Output 1" width="900"> </p>
🖼️ Output 2
<p align="center"> <img src="./Images/Output2.png" alt="AutoGen Multi-Agent Morning Coordinator - Output 2" width="900"> </p>
🖼️ Output 3
<p align="center"> <img src="./Images/Output3.png" alt="AutoGen Multi-Agent Morning Coordinator - Output 3" width="900"> </p>

-----

## 🔄 Workflow

```text
                         👤 User
                           │
                           ▼
                  🎨 Streamlit UI
                           │
                           ▼
                   🤖 AutoGen Team
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   School Agent 1   School Agent 2    Office Agent
          │                │                │
          ▼                ▼                ▼
        Kid 1            Kid 2           Father
     School A          School B          Office
     8:00 AM           8:15 AM           9:00 AM
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                  🧠 Coordinated Plan
                           │
                           ▼
                       ✅ Result
