from fastapi import APIRouter


router = APIRouter(tags=['테스트 (Default)'])

@router.get("/", summary="서버 테스트")
def root():
    return {"message": "Community FastAPI Server is running"}
