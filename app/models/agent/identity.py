from pydantic import BaseModel

class Identity(BaseModel):
    name: str
    age: int
    