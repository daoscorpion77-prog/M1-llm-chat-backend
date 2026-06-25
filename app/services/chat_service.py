from app.core.config import settings


class ChatService:
    @staticmethod
    def chat(message: str):
        return f"[{settings.LLM_MODEL}] 你说的是：{message}"