from fastapi import Depends, APIRouter, HTTPException
from schemas.post import PostCreate, PostUpdate, PostResponse, PostListResponse
from sqlalchemy.orm import Session
from database import get_db
from controller.post import create_post_controller, get_posts_controller, get_post_specific_controller, delete_post_controller, update_post_controller


router = APIRouter(prefix = "/posts", tags=['게시글 (Posts)'])

@router.post("", response_model=PostResponse, summary="게시글 생성")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return create_post_controller(db, post)

@router.get("", response_model=list[PostListResponse], summary="게시글 목록 조회")
def get_posts(db: Session = Depends(get_db)):
    return get_posts_controller(db)

@router.get("/{post_id}", response_model=PostResponse, summary="특정 게시글 조회")
def get_post_specific(post_id: int, db: Session = Depends(get_db)):
    post = get_post_specific_controller(db, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")

    return post

@router.delete("/{post_id}", summary="게시글 삭제")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = delete_post_controller(db, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")

    return {
        "deleted_post_id": post_id,
        "message": "게시글이 삭제되었습니다."
    }

@router.patch("/{post_id}", response_model=PostResponse, summary="게시글 수정")
def update_post(
    post_id: int,
    post_update: PostUpdate,
    db: Session = Depends(get_db)
):
    post = update_post_controller(db, post_id, post_update)

    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")

    return post
