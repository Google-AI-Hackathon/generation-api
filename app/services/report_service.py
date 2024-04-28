from app.prompts.report import report_prompt
from app.models.conversation.interaction import InteractionResponse
from app.services.llm_service import generate_response

def generate_report(conversation_interactions: list[InteractionResponse]):
    return generate_response(report_prompt(conversation_interactions))