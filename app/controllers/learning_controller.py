from app.services.learning_service import create_mind_map, create_guide_book

from app.models.learning.mind_map import MindMap
from app.models.learning.learning import LearningRequest

def create_mind_map_controller(learning_request: LearningRequest):
    return create_mind_map(learning_request)

def create_guide_book_controller(learning_request: LearningRequest, mind_map: MindMap):
    return create_guide_book(learning_request, mind_map)