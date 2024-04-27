from pydantic import BaseModel
from typing import List
from enum import Enum

class Level(str, Enum):
    novice = "novice"
    intermediate = "intermediate"
    proficient = "proficient"
    expert = "expert"

class Expertise(BaseModel):
    domain: str
    subdomains: List[str]
    level: Level
    thinking_process: str