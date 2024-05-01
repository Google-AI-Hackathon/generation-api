from fastapi import APIRouter
from typing import List

from app.controllers.conversation_controller import create_conversation_controller
from app.models.conversation.conversation import ConversationRequest
from app.models.interaction.interaction import InteractionResponse

from app.utils.response import interaction_as_response
from app.utils.record import save_conversation

router = APIRouter()

@router.post("/", response_model=List[InteractionResponse])
async def create_conversation(request: ConversationRequest) -> List[InteractionResponse]:
    conversation = create_conversation_controller(request.participants)
    if request.save:
        save_conversation(conversation, request.title)
    return [interaction_as_response(interaction) for interaction in conversation.interactions]