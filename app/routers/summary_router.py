from fastapi import APIRouter
from typing import List

from app.controllers.summary_controller import create_summary_controller
from app.models.interaction.interaction import InteractionResponse

router = APIRouter()

@router.post("/", response_model=str)
async def create_summary(conversation_interactions: List[InteractionResponse]) -> str:
    return create_summary_controller(conversation_interactions)