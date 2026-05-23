from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class CommentCreate(BaseModel):
    content: str
    author: str

class CommentUpdate(BaseModel):
    content: Optional[str] = None
    author: Optional[str] = None

class CommentResponse(BaseModel):
    id: int
    post_id: int
    content: str
    author: str
    created_at: datetime
