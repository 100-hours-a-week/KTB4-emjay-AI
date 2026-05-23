from fastapi import Depends, APIRouter
from schemas.post import PostCreate, PostResponse
from sqlalchemy.orm import Session
from database import get_db
from controller.post import create_post_controller


router = APIRouter(tags=['게시글 (Posts)'])

@router.post("/posts", response_model=PostResponse, summary="게시글 생성")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return create_post_controller(db, post)
