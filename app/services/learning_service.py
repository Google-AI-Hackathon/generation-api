from app.prompts.learning import mind_map_prompt
from app.models.learning.learning import LearningRequest
from app.models.learning.mind_map import MindMap

from app.services.llm_service import generate_response

def create_mind_map(learning_request: LearningRequest) -> MindMap:
    response = generate_response(mind_map_prompt(learning_request))
    return response
    return MindMap(**eval(response))