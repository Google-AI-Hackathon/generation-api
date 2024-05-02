from fastapi import APIRouter

from app.controllers.learning_controller import create_mind_map_controller, create_guide_book_controller
from app.models.learning.learning import LearningRequest, GuideBookRequest, MindMap

router = APIRouter()

@router.post("/mind-map", response_model=MindMap)
async def create_mind_map(request: LearningRequest) ->  MindMap:
    return create_mind_map_controller(request)

@router.post("/guide-book", response_model=str)
async def create_guide_book(request: GuideBookRequest) -> str:
    return create_guide_book_controller(request.learning_request, request.mind_map)