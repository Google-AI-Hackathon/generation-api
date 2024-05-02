import os
import google.generativeai as genai

MODEL_NAME = 'gemini-pro'
TEMPERATURE = 0.0

LLM = genai.GenerativeModel(
    MODEL_NAME,
    generation_config=genai.GenerationConfig(
        temperature=TEMPERATURE,
    ))

# Conversation Configuration
MAX_CONVERSATION_CONTEXT_INTERACTIONS = 4

# Podcast Configuration
MAX_PODCAST_CONTEXT_INTERACTIONS = 3

TTS_LANGUAGE = 'en-US'