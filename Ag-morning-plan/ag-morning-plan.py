import asyncio
import os

from dotenv import load_dotenv
import streamlit as st

from typing import AsyncGenerator, Any

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_ext.models.openai import OpenAIChatCompletionClient


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AutoGen Morning Plan",
    layout="wide"
)

st.title("🤖 AutoGen Multi-Agent Morning Coordinator")


# ==========================================
# Environment Setup & Sidebar
# ==========================================

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY", "")

st.sidebar.header("⚙️ Configuration")

api_key = st.sidebar.text_input(
    "Gemini API Key",
    value=gemini_key,
    type="password"
)


# ==========================================
# Task Definition
# ==========================================

task_description = """
It is 7:30 AM at home.

Father has three responsibilities:

1. Kid 1 needs to go to School A (Arrive by 8:00 AM)
2. Kid 2 needs to go to School B (Arrive by 8:15 AM)
3. Father needs to go to Office (Arrive by 9:00 AM)

Create a coordinated plan ensuring all deadlines are met.
"""

st.info(f"**Task:** {task_description}")


# ==========================================
# Core AutoGen Logic
# ==========================================

async def get_team_stream(
    task: str,
    key: str
) -> AsyncGenerator[Any, None]:

    model_client = OpenAIChatCompletionClient(
        model="gemini-3-flash-preview",
        api_key=key,
        base_url=(
            "https://generativelanguage.googleapis.com/"
            "v1beta/openai/"
        ),
        model_info={
            "vision": True,
            "function_calling": True,
            "json_output": True,
            "structured_output": True,
            "family": "gemini",
        }
    )

    # ==========================================
    # Define Agents
    # ==========================================

    agent1 = AssistantAgent(
        name="School_Agent_1",
        model_client=model_client,
        system_message="""
You are School Agent 1.

Responsibility:
Take Kid 1 to School A.

Deadline:
Must arrive before 8:00 AM.

Create a specific plan with realistic times.

Do not handle Kid 2 or Father's office.
"""
    )

    agent2 = AssistantAgent(
        name="School_Agent_2",
        model_client=model_client,
        system_message="""
You are School Agent 2.

Responsibility:
Take Kid 2 to School B.

Deadline:
Must arrive before 8:15 AM.

Create a specific plan with realistic times.

Do not handle Kid 1 or Father's office.
"""
    )

    agent3 = AssistantAgent(
        name="Office_Agent",
        model_client=model_client,
        system_message="""
You are the Office Agent.

Responsibility:
Take Father to Office.

Deadline:
Must arrive before 9:00 AM.

Review the plans from School Agent 1
and School Agent 2.

Ensure all three plans exist and
are timed realistically.

If everything is coordinated, say exactly:

ALL TASKS COMPLETED TERMINATE
"""
    )

    # ==========================================
    # Termination Condition
    # ==========================================

    termination = TextMentionTermination("TERMINATE")

    # ==========================================
    # Group Chat Team
    # ==========================================

    team = RoundRobinGroupChat(
        participants=[
            agent1,
            agent2,
            agent3
        ],
        termination_condition=termination
    )

    # ==========================================
    # Stream Messages
    # ==========================================

    async for message in team.run_stream(task=task):
        yield message

    await model_client.close()


# ==========================================
# Streamlit Session State
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================
# Display Previous Messages
# ==========================================

for msg in st.session_state.messages:

    with st.chat_message(msg["source"]):
        st.write(msg["content"])


# ==========================================
# Start Planning
# ==========================================

if st.sidebar.button(
    "🚀 Start Planning",
    type="primary"
):

    if not api_key:

        st.error(
            "Please enter a valid Gemini API Key."
        )

    else:

        st.session_state.messages = []

        async def run_workflow():

            with st.status(
                "🤖 Planning in progress...",
                expanded=True
            ) as status:

                try:

                    async for message in get_team_stream(
                        task_description,
                        api_key
                    ):

                        source = getattr(
                            message,
                            "source",
                            "System"
                        )

                        content = getattr(
                            message,
                            "content",
                            str(message)
                        )

                        if not content:
                            continue

                        st.session_state.messages.append(
                            {
                                "source": source,
                                "content": content
                            }
                        )

                        with st.chat_message(source):
                            st.write(content)

                    status.update(
                        label="✅ Planning Completed!",
                        state="complete",
                        expanded=False
                    )

                except Exception as e:

                    status.update(
                        label="❌ Error occurred",
                        state="error",
                        expanded=True
                    )

                    st.error(
                        f"Execution Error: {e}"
                    )

        asyncio.run(run_workflow())