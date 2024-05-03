from pydantic import BaseModel
from typing import List

from app.models.agent.agent import Agent

from app.models.podcast.style import Style
from app.models.option.depth import Depth
from app.models.option.detail import DetailLevel

from app.models.interaction.interaction import Interaction, InteractionResponse
from app.models.interaction.counter import Counter

class Podcast(BaseModel):
    topic: str
    style: Style
    depth: Depth
    detail_level: DetailLevel
    
class IndividualPodcast(Podcast):
    speaker: Agent
    
class DualPodcast(Podcast):
    n_interactions: int
    host: Agent
    participant: Agent
    interactions: List[Interaction]
    counter: Counter
    
class PodcastResponse(BaseModel):
    interactions: List[InteractionResponse]
    public_url: str
    
class PodcastRequest(BaseModel):
    topic: str
    style: Style
    depth: Depth
    detail_level: DetailLevel
    n_interactions: int
    host: Agent
    participant: Agent