from pydantic import BaseModel
from typing import Any, Optional


class ResponseModel(BaseModel):
    code: int = 0
    message: str = "success"
    data: Any = None
    trace_id: Optional[str] = None