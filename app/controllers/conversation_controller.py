from app.services.conversation_service import initialize_conversation, run_conversation

from app.models.agent.conversational_agent import ConversationalAgent
from app.models.conversation.conversation import Conversation

def create_conversation_controller(agents: list[ConversationalAgent]) -> Conversation:
    conversation = initialize_conversation(agents)
    run_conversation(conversation)
    return conversation