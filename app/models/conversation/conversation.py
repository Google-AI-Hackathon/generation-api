from pydantic import BaseModel
from typing import List
from app.models.interaction.interaction import Interaction
from app.models.interaction.counter import Counter
from app.models.agent.conversational_agent import ConversationalAgent

class Conversation(BaseModel):
    n_interactions: int
    participants: List[ConversationalAgent]
    interactions: List[Interaction]
    counter: Counter
    
class ConversationRequest(BaseModel):
    title: str
    n_interactions: int
    participants: List[ConversationalAgent]
    save: bool