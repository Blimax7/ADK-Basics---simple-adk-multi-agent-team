import os
import asyncio
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

GROQ_MODEL = LiteLlm(model="groq/llama-3.3-70b-versatile")

# ── Tools ──────────────────────────────────────────────

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city."""
    print(f"--- Tool: get_weather called for city: {city} ---")
    city_normalized = city.lower().replace(" ", "")

    mock_weather_db = {
        "newyork": {"status": "success", "report": "The weather in New York is sunny with a temperature of 25°C."},
        "london":  {"status": "success", "report": "It's cloudy in London with a temperature of 15°C."},
        "tokyo":   {"status": "success", "report": "Tokyo is experiencing light rain and a temperature of 18°C."},
    }

    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {"status": "error", "error_message": f"Sorry, I don't have weather information for '{city}'."}


def say_hello(name: str = None) -> str:
    """Provides a friendly greeting, optionally using the person's name."""
    if name:
        print(f"--- Tool: say_hello called with name: {name} ---")
        return f"Hello, {name}! Great to meet you!"
    print("--- Tool: say_hello called ---")
    return "Hello there! How can I help you today?"


def say_goodbye() -> str:
    """Provides a farewell message."""
    print("--- Tool: say_goodbye called ---")
    return "Goodbye! Have a wonderful day!"


# ── Sub-Agents ─────────────────────────────────────────

greeting_agent = Agent(
    name="greeting_agent",
    model=GROQ_MODEL,
    description="Handles simple greetings and hellos using the say_hello tool.",
    instruction=(
        "You are the Greeting Agent. Your ONLY task is to greet the user. "
        "Use the 'say_hello' tool to generate the greeting. "
        "If the user provides their name, pass it to the tool. "
        "Do not do anything else."
    ),
    tools=[say_hello],
)

farewell_agent = Agent(
    name="farewell_agent",
    model=GROQ_MODEL,
    description="Handles farewells and goodbyes using the say_goodbye tool.",
    instruction=(
        "You are the Farewell Agent. Your ONLY task is to say goodbye. "
        "Use the 'say_goodbye' tool when the user says bye, goodbye, or see you. "
        "Do not do anything else."
    ),
    tools=[say_goodbye],
)

# ── Root Agent ─────────────────────────────────────────

root_agent = Agent(
    name="weather_agent",
    model=GROQ_MODEL,
    description="Main coordinator agent. Handles weather requests and delegates greetings and farewells to specialists.",
    instruction=(
        "You are the main Weather Agent coordinating a team. "
        "Use the 'get_weather' tool ONLY for weather requests. "
        "Delegate greetings like 'Hi' or 'Hello' to 'greeting_agent'. "
        "Delegate farewells like 'Bye' or 'Goodbye' to 'farewell_agent'. "
        "For anything else, politely say you can only help with weather, greetings, and farewells."
    ),
    tools=[get_weather],
    sub_agents=[greeting_agent, farewell_agent],
)