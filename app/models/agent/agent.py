from pydantic import BaseModel

from app.models.agent.identity import Identity
from app.models.agent.personality import Personality
from app.models.agent.background import Background
from app.models.agent.expertise import Expertise
from app.models.agent.mood import Mood

class Agent(BaseModel):
    identity: Identity
    personality: Personality
    background: Background
    expertise: Expertise
    mood: Mood