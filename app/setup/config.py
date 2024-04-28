import google.generativeai as genai

MODEL_NAME = 'gemini-pro'
TEMPERATURE = 0.5

LLM = genai.GenerativeModel(
    MODEL_NAME,
    generation_config=genai.GenerationConfig(
        temperature=TEMPERATURE,
    ))

MAX_CONVERSATION_AGENTS = 4
MAX_AGENT_INTERACTIONS = 8
MAX_CONTEXT_INTERACTIONS = 7