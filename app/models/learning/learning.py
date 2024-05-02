from pydantic import BaseModel
from typing import List

from app.models.learning.mind_map import MindMap
from app.models.option.depth import Depth
from app.models.option.detail import DetailLevel
from app.models.option.terminology import Terminology


class LearningRequest(BaseModel):
    topic: str
    keywords: List[str]
    terminology: Terminology
    depth: Depth
    detail_level: DetailLevel
    
class GuideBookRequest(BaseModel):
    learning_request: LearningRequest
    mind_map: MindMap