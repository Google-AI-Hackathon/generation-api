from enum import Enum

class Depth(str, Enum):
    shallow = 'shallow'
    intermediate = 'intermediate'
    deep = 'deep'