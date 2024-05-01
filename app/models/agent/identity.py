from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class Identity(BaseModel):
    name: str
    age: int
    gender: Gender