from fastapi import FastAPI
from database import engine, Base
from router.default import router as default_router
from router.post import router as post_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(default_router)
app.include_router(post_router)
