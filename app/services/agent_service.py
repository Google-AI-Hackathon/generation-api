from app.models.agent.agent import Agent
from app.models.conversation.conversation import Conversation

from app.prompts.agent import single_interaction_prompt, conversational_interaction_prompt
from app.services.llm_service import generate_response

def generate_single_interaction_response(agent: Agent, prompt: str) -> str:
    return generate_response(single_interaction_prompt(agent, prompt))

def generate_conversation_interaction_response(agent: Agent, conversation: Conversation) -> str:
    return generate_response(conversational_interaction_prompt(agent, conversation))