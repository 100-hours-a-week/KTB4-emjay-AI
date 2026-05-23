from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas.summary import SummaryResponse
from controller.summary import summarize_post_with_comments_controller


router = APIRouter(prefix="/posts", tags=["AI 요약 (Summary)"])

@router.post("/{post_id}/summary", response_model=SummaryResponse, summary="게시글 및 댓글 종합 요약")
def summarize_post_with_comments(post_id: int,db: Session = Depends(get_db)):
    try:
        summary = summarize_post_with_comments_controller(db, post_id)

        if summary is None:
            raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")

        return SummaryResponse(summary=summary)

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI 요약 실패: {str(e)}")
