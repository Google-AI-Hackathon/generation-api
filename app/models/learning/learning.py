from pydantic import BaseModel
from typing import List

from app.models.option.depth import Depth
from app.models.option.detail import DetailLevel
from app.models.option.terminology import Terminology


class LearningRequest(BaseModel):
    topic: str
    keywords: List[str]
    terminology: Terminology
    depth: Depth
    detail_level: DetailLevel