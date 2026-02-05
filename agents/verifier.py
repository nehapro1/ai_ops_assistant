import json
from llm.groq_client import chat

def verify_and_finalize(user_query, execution_results):
    system_prompt = """
    You are the Verifier. Review the tool outputs and provide a final answer.
    If the data is missing or wrong, explain why.
    Respond ONLY in JSON format:
    {"status": "complete", "answer": "The weather in London is 15°C and here are the top repos..."}
    """
    
    prompt = f"Original Task: {user_query}\nResults Found: {json.dumps(execution_results)}"
    response = chat(prompt, system_prompt)
    return json.loads(response)