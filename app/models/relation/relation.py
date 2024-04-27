from pydantic import BaseModel
from typing import List
from enum import Enum

from app.models.agent.agent import Agent

class Hierarchy(str, Enum):
    unknown = "unknown"
    familial = "familial"
    friendship = "friendship"
    partnership = "partnership"
    mentorship = "mentorship"

class Style(str, Enum):
    neutral = "neutral"
    friendly = "friendly"
    professional = "professional"
    
class Intent(str, Enum):
    neutral = "neutral"
    cooperative = "cooperative"
    competitive = "competitive"
    
class Relation(BaseModel):
    other: Agent
    hierarchy: Hierarchy
    style: Style
    intent: Intent