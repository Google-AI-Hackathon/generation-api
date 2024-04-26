from app.setup.config import MAX_CONTEXT_INTERACTIONS
from app.models.conversation.interaction import Interaction
from app.models.conversation.conversation import Conversation

def interaction_as_context(interaction: Interaction) -> str:
    return f"""
[{interaction.agent.identity.name}]: {interaction.message}
"""

def get_context(conversation: Conversation) -> str:
    context = ""
    for interaction in conversation.interactions[-MAX_CONTEXT_INTERACTIONS:]:
        context += interaction_as_context(interaction)
    return context