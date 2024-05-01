from pydantic import BaseModel
from typing import List, Dict

class Counter(BaseModel):
    remaining_interactions: Dict[str, int]