from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.comment import CommentCreate, CommentUpdate, CommentResponse
from controller.comment import create_comment_controller, get_comments_controller, update_comment_controller, delete_comment_controller


router = APIRouter(prefix="/posts/{post_id}/comments",tags=["댓글 (Comments)"])

@router.post("", response_model=CommentResponse, summary="댓글 작성")
def create_comment(
    post_id: int,
    comment: CommentCreate,
    db: Session = Depends(get_db)
):
    created_comment = create_comment_controller(db, post_id, comment)

    if not created_comment:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")

    return created_comment

@router.get("", response_model=list[CommentResponse], summary="특정 게시글의 댓글 목록 조회")
def get_comments(post_id: int, db: Session = Depends(get_db)):
    comments = get_comments_controller(db, post_id)

    if comments is None:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")

    return comments

@router.patch("/{comment_id}", response_model=CommentResponse, summary="특정 게시글의 댓글 수정")
def update_comment(
    post_id: int,
    comment_id: int,
    comment_update: CommentUpdate,
    db: Session = Depends(get_db)
):
    updated_comment = update_comment_controller(
        db,
        post_id,
        comment_id,
        comment_update
    )

    if not updated_comment:
        raise HTTPException(status_code=404, detail="댓글을 찾을 수 없습니다.")

    return updated_comment

@router.delete("/{comment_id}", summary="특정 게시글의 댓글 삭제")
def delete_comment(
    post_id: int,
    comment_id: int,
    db: Session = Depends(get_db)
):
    deleted_comment = delete_comment_controller(db, post_id, comment_id)

    if not deleted_comment:
        raise HTTPException(status_code=404, detail="댓글을 찾을 수 없습니다.")

    return {
        "deleted_comment_id": comment_id,
        "message": "댓글이 삭제되었습니다."
    }
