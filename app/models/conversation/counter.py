from pydantic import BaseModel
from typing import Dict

class Counter(BaseModel):
    remaining_interactions: Dict[str, int]