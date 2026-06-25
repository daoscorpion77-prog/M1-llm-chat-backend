from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(
    title="LLM Chat Backend",
    description="A FastAPI backend for LLM application development.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(chat_router, prefix="/api")