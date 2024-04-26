import google.generativeai as genai

MODEL_NAME = 'gemini-pro'
TEMPERATURE = 1.0

LLM = genai.GenerativeModel(
    MODEL_NAME,
    generation_config=genai.GenerationConfig(
        temperature=TEMPERATURE,
    ))