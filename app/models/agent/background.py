from pydantic import BaseModel
from typing import List

class Background(BaseModel):
    background_story: str
    memories: List[str]
    interests: List[str]