from pydantic import BaseModel

from app.models.agent.agent import Agent

class Interaction(BaseModel):
    agent: Agent
    message: str
    
class InteractionResponse(BaseModel):
    agent_name: str
    message: str