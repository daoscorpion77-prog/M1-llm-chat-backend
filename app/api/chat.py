from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.schemas.base import ResponseModel
from app.services.chat_service import ChatService
import uuid

router = APIRouter()


@router.post("/chat", response_model=ResponseModel)
def chat(req: ChatRequest):

    # 1. 生成 trace_id
    trace_id = str(uuid.uuid4())

    # 2. 调用 service
    answer = ChatService.chat(req.message)

    # 3. 返回统一结构
    return ResponseModel(
        code=0,
        message="success",
        data={
            "answer": answer
        },
        trace_id=trace_id
    )