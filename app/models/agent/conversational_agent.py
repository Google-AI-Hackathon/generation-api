from typing import List

from app.models.agent.agent import Agent
from app.models.relation.relation import Relation

class ConversationalAgent(Agent):
    goal: str
    relations: List[Relation]