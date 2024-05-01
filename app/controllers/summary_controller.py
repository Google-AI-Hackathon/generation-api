from app.services.summary_service import generate_summary
from app.models.interaction.interaction import InteractionResponse

def create_summary_controller(conversation_interactions: list[InteractionResponse]):
    return generate_summary(conversation_interactions)