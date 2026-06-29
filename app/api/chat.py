import uuid
from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.schemas.base import ResponseModel
from app.services.chat_service import (
    ChatService,
    LLMConfigError,
    LLMProviderError,
    LLMResponseParseError,
)

router = APIRouter()


@router.post("/chat", response_model=ResponseModel)
def chat(req: ChatRequest):
    # 1. 生成 trace_id
    trace_id = str(uuid.uuid4())

    try:
        # 2. 调用 service
        answer = ChatService.chat(req.message)

        # 3. 成功返回
        return ResponseModel(
            code=0,
            message="success",
            data={
                "answer": answer
            },
            trace_id=trace_id
        )

    except LLMConfigError as e:
        return ResponseModel(
            code=1001,
            message=str(e),
            data=None,
            trace_id=trace_id
        )

    except LLMProviderError as e:
        return ResponseModel(
            code=1002,
            message=str(e),
            data=None,
            trace_id=trace_id
        )

    except LLMResponseParseError as e:
        return ResponseModel(
            code=1003,
            message=str(e),
            data=None,
            trace_id=trace_id
        )

    except Exception:
        return ResponseModel(
            code=5000,
            message="服务器内部错误",
            data=None,
            trace_id=trace_id
        )