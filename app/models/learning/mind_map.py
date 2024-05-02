from pydantic import BaseModel
from typing import List

class Node(BaseModel):
    title: str
    children: List['Node'] = []

class MindMap(BaseModel):
    title: str
    children: List[Node]