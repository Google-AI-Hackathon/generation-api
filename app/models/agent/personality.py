from enum import Enum
from pydantic import BaseModel

class SocialOrientation(str, Enum):
    introverted = "introverted"
    extroverted = "extroverted"
    
class InformationProcessing(str, Enum):
    intuitive = "intuitive"
    sensing = "sensing"

class DecisionMakingStyle(str, Enum):
    thinking = "thinking"
    feeling = "feeling"

class ApproachToStructure(str, Enum):
    judging = "judging"
    perceiving = "perceiving"

class Personality(BaseModel):
    social_orientation: SocialOrientation
    information_processing: InformationProcessing
    decision_making_style: DecisionMakingStyle
    approach_to_structure: ApproachToStructure