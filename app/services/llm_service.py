from app.setup.config import LLM

def generate_response(prompt: str) -> str:
    response = LLM.generate_content(prompt)
    return response

def generate_response_text(prompt: str) -> str:
    response = LLM.generate_content(prompt)
    return response.text

def evaluate_response(response):
    return response.prompt_feedback