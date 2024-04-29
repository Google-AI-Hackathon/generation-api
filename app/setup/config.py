import google.generativeai as genai
import os
MODEL_NAME = 'gemini-pro'
TEMPERATURE = 0.5

LLM = genai.GenerativeModel(
    MODEL_NAME,
    generation_config=genai.GenerationConfig(
        temperature=TEMPERATURE,
    ))

# Conversation Config 
MAX_CONVERSATION_AGENTS = os.getenv('MAX_CONVERSATION_AGENTS') or 8
MAX_AGENT_INTERACTIONS = os.getenv('MAX_AGENT_INTERACTIONS') or 7
MAX_CONTEXT_INTERACTIONS = os.getenv('MAX_CONTEXT_INTERACTIONS') or 3

# TTS Config
TTS_LANGUAGE = os.getenv('TTS_LANGUAGE') or 'en-US'