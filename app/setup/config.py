import google.generativeai as genai

MODEL_NAME = 'gemini-pro'
TEMPERATURE = 1.0

LLM = genai.GenerativeModel(
    MODEL_NAME,
    generation_config=genai.GenerationConfig(
        temperature=TEMPERATURE,
    ))

MAX_CONVERSATION_AGENTS = 4
MAX_AGENT_INTERACTIONS = 4
MAX_CONTEXT_INTERACTIONS = 4