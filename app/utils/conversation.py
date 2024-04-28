import random

from app.models.conversation.conversation import Conversation
from app.models.conversation.interaction import Interaction, InteractionResponse

def shuffle_participants(conversation: Conversation):
    random.shuffle(conversation.participants)
    
def get_interaction_response(interaction: Interaction) -> InteractionResponse:
    return InteractionResponse(agent_name=interaction.agent.identity.name, message=interaction.message)