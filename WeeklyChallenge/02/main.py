from fastapi import FastAPI
from database import engine, Base

from router.default import router as default_router
from router.post import router as post_router
from router.comment import router as comment_router
from router.summary import router as summary_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(default_router)
app.include_router(post_router)
app.include_router(comment_router)
app.include_router(summary_router)
