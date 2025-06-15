
import requests

def call_mistral(prompt: str, context: list):
    full_prompt = f"have known tasks：{context}\\n user: {prompt}\\n:"
    response = requests.post(
        "http://host.docker.internal:11434/api/generate", 
        json={"model": "mistral", "prompt": full_prompt, "stream": False}
    )
    return response.json().get("response", "sorry, I cant handle this request")
