import os
from groq import Groq
from dotenv import load_dotenv  


load_dotenv() 

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY missing at runtime")


client = Groq(api_key=api_key)

def chat(prompt: str, system_message: str = "You are a helpful assistant."):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"} 
    )
    return completion.choices[0].message.content