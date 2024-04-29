
from pydantic import BaseModel
from enum import Enum


class Gender (Enum):
    MALE = 1
    FEMALE = 2

class Voice(BaseModel):
    name: str
    ssml_gender: Gender

    def __str__(self):
        return f"{self.name} - {self.ssml_gender}"
    


    
 