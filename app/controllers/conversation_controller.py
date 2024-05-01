from app.services.conversation_service import initialize_conversation, run_conversation

from app.models.agent.conversational_agent import ConversationalAgent
from app.models.conversation.conversation import Conversation

def create_conversation_controller(title: str, agents: list[ConversationalAgent], n_interactions: int) -> Conversation:
    conversation = initialize_conversation(title, agents, n_interactions)
    run_conversation(conversation)
    return conversation