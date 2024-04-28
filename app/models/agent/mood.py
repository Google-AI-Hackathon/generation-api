from pydantic import BaseModel
from typing import List
from enum import Enum

class ThinkingFlexibility(str, Enum):
    consistent = "consistent"
    adaptable = "adaptable"
    
class ExpectationAttitude(str, Enum):
    realistic = "realistic"
    optimistic = "optimistic"
    pessimistic = "pessimistic"
    
class ElaborationLength(str, Enum):
    concise = "concise"
    moderate = "moderate"
    verbose = "verbose"

class Mood(BaseModel):
    social_tone: List[str]
    emotional_tone: List[str]
    mental_tone: List[str]
    thinking_flexibility: ThinkingFlexibility
    expectation_attitude: ExpectationAttitude
    elaboration_length: ElaborationLength