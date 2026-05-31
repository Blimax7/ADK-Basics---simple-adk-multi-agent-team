# ADK Basics - Simple ADK Multi-Agent Team

A multi-agent AI system built with **Google Agent Development Kit (ADK)** and **Groq Cloud**.

Features a root **Weather Agent** that intelligently delegates greetings and farewells to specialized sub-agents, all powered by **LLaMA 3.3 70B** — completely free, no Google API key required.

---

## 🤖 Agent Team Structure

- **Root Agent** (`weather_agent`) — Handles weather requests and coordinates the team
  - **Sub-Agent** (`greeting_agent`) — Handles greetings using the `say_hello` tool
  - **Sub-Agent** (`farewell_agent`) — Handles farewells using the `say_goodbye` tool

---

## 🛠️ Tech Stack

- [Google ADK](https://google.github.io/adk-docs/) - Agent Development Kit
- [Groq Cloud](https://console.groq.com) - Free LLM API
- [LiteLLM](https://docs.litellm.ai/) - Model integration bridge
- Python 3.10+

---

## ⚙️ Setup

### 1. Clone the repository
git clone https://github.com/Blimax7/ADK-Basics---simple-adk-multi-agent-team.git
cd ADK-Basics---simple-adk-multi-agent-team

### 2. Create and activate virtual environment
python -m venv venv

# Windows PowerShell
venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate

### 3. Install dependencies
pip install google-adk litellm python-dotenv

### 4. Add your Groq API key
Create a `.env` file inside the `multi_agent_team/` folder:
GROQ_API_KEY=your_actual_groq_api_key_here

Get your free API key at [console.groq.com](https://console.groq.com)

---

## 🚀 Run the Agent

adk web

Then open your browser at **http://localhost:8000** and select `multi_agent_team` from the dropdown.

---

## 💬 Example Prompts

- `Hello!`
- `Hi, my name is John`
- `What is the weather in London?`
- `What is the weather in Tokyo?`
- `What is the weather in Paris?`
- `Goodbye!`

---

## 📁 Project Structure

ADK_Groq_Multi_Agent_Team/
└── multi_agent_team/
    ├── __init__.py   → Registers the agent package
    ├── agent.py      → Defines tools, sub-agents, and root agent
    └── .env          → Stores your Groq API key (not uploaded)

---

## 🔄 How Delegation Works

1. User sends a message to the **root agent**
2. Root agent analyzes the intent:
   - Weather request → handles it directly using `get_weather` tool
   - Greeting → delegates to `greeting_agent`
   - Farewell → delegates to `farewell_agent`
3. The appropriate agent responds using its specialized tool

---

## 📌 Notes

- `.env` is excluded from the repository via `.gitignore` to protect your API key
- Built-in ADK tools like `google_search` are not supported with third-party LLMs
- Only custom Python function tools work with Groq via LiteLLM
- If you edit `agent.py` while `adk web` is running, restart the server with `Ctrl+C` then `adk web`
