# schemas的作用是规定前端能够传什么

from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str