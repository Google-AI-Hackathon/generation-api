from pydantic import BaseModel
from typing import List

from app.models.conversation.interaction import Interaction
from app.models.conversation.counter import Counter
from app.models.agent.agent import Agent

class Conversation(BaseModel):
    topic: str
    goal: str
    participants: List[Agent]
    interactions: List[Interaction]
    counter: Counter