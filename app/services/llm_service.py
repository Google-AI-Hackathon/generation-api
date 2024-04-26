from app.setup.config import LLM

def generate_response(prompt: str) -> str:
    response = LLM.generate_content(prompt)
    return response.text