import json
from llm.openai_client import chat

def plan_task(user_input: str):
    system_prompt = """
    You are a Planner Agent. Your job is to break a user's request into steps using available tools.
    
    Available tools:
    1. get_weather: Requires a 'city' argument (e.g., {"city": "London"}).
    2. search_github: Requires a 'query' argument (e.g., {"query": "python web framework"}).
    
    Constraint: Respond ONLY in valid JSON format.
    
    Example Output for "What is the weather in Paris and find me FastAPI repos":
    {
      "steps": [
        {"step": 1, "tool": "get_weather", "args": {"city": "Paris"}},
        {"step": 2, "tool": "search_github", "args": {"query": "FastAPI"}}
      ]
    }
    """
    response = chat(user_input, system_prompt)
    return json.loads(response)