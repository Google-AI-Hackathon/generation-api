from enum import Enum

class DetailLevel(str, Enum):
    superficial = 'superficial'
    intermediate = 'intermediate'
    detailed = 'detailed'