from app.prompts.summary import summary_prompt
from app.models.interaction.interaction import InteractionResponse
from app.services.llm_service import generate_response

def generate_summary(conversation_interactions: list[InteractionResponse]):
    return generate_response(summary_prompt(conversation_interactions))