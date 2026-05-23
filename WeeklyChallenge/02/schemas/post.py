from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class PostCreate(BaseModel):
    title: str
    content: str
    author: str
    
class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    author: str
    comment_count: int
    view_count: int
    created_at: datetime

class PostListResponse(BaseModel):
    id: int
    title: str
    author: str
    comment_count: int
    view_count: int
    created_at: datetime
