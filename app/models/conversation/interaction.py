from pydantic import BaseModel

from app.models.agent.agent import Agent

class Interaction(BaseModel):
    agent: Agent
    message: str