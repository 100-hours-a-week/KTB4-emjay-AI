from datetime import datetime
from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str
    author: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    author: str
    comment_count: int
    view_count: int
    created_at: datetime
