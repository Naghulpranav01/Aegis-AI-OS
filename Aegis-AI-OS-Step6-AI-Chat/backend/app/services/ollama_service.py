import requests
from app.core.config import OLLAMA_URL,MODEL

def chat(prompt:str):
    try:
        r=requests.post(f"{OLLAMA_URL}/api/generate",
            json={"model":MODEL,"prompt":prompt,"stream":False},timeout=120)
        r.raise_for_status()
        return r.json().get("response","")
    except Exception as e:
        return f"Error: {e}"
