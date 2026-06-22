from fastapi import FastAPI

app = FastAPI(
    title="LLM Chat Backend",
    description="A FastAPI backend for LLM application development.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}