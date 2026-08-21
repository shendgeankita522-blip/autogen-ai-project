# 🤖 AutoGen Multi-Agent Morning Coordinator

An interactive **Multi-Agent AI application** built using **Microsoft AutoGen, Google Gemini, Python, and Streamlit**.

The application uses multiple specialized AI agents to coordinate a family's morning schedule and create a realistic plan while ensuring that all specified deadlines are met.

---

## 📌 Project Overview

Imagine it is **7:30 AM** and a father has three responsibilities:

- 👦 Kid 1 needs to reach **School A by 8:00 AM**
- 👧 Kid 2 needs to reach **School B by 8:15 AM**
- 👨 Father needs to reach **Office by 9:00 AM**

Instead of asking one AI agent to handle everything, this project uses multiple specialized agents.

Each agent has a specific responsibility and contributes to the final coordinated plan.

### Multi-Agent Architecture

```text
                         👤 User
                           │
                           ▼
                  ┌─────────────────┐
                  │   Streamlit UI  │
                  └────────┬────────┘
                           │
                           ▼
                   🤖 AutoGen Team
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
      👦 School Agent 1  👧 School Agent 2  👨 Office Agent
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                  🧠 Coordinated Plan
                           │
                           ▼
                     ✅ Final Result
