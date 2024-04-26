from pydantic import BaseModel
from typing import List
from enum import Enum

class Flexibility(str, Enum):
    consistent = "consistent"
    adaptable = "adaptable"
    
class Attitude(str, Enum):
    optimistic = "optimistic"
    pessimistic = "pessimistic"

class Mood(BaseModel):
    social_tone: List[str]
    emotional_tone: List[str]
    mental_tone: List[str]
    flexibility: Flexibility
    attitude: Attitude