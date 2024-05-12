from pydantic import BaseModel
from typing import List

class Comment(BaseModel):
    text: str
    author: str

class Post(BaseModel):
    title: str
    content: str
    author: str
    comments: List[Comment] = []
    likes: int = 0
    dislikes: int = 0
