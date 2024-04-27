from pydantic import BaseModel
from typing import List

from app.models.conversation.interaction import Interaction
from app.models.conversation.counter import Counter
from app.models.agent.agent import Agent
from app.models.agent.conversational_agent import ConversationalAgent

class Conversation(BaseModel):
    participants: List[ConversationalAgent]
    interactions: List[Interaction]
    counter: Counter
    
class ConversationRequest(BaseModel):
    title: str
    participants: List[ConversationalAgent]
    save: bool