import httpx
from app.core.config import settings

class LLMConfigError(Exception):
    """大模型配置错误，例如没有设置 API Key。"""
    pass


class LLMProviderError(Exception):
    """大模型服务请求错误，例如超时、状态码错误。"""
    pass


class LLMResponseParseError(Exception):
    """大模型返回格式解析错误。"""
    pass


class ChatService:
    @staticmethod
    def chat(message: str) -> str:
        # 1. 检查 API Key
        if not settings.DEEPSEEK_API_KEY:
            raise LLMConfigError("未设置 DEEPSEEK_API_KEY，请先在本地 .env 文件中配置真实 API Key")

        # 2. 组装请求地址
        url = f"{settings.DEEPSEEK_BASE_URL.rstrip('/')}/chat/completions"

        # 3. 组装请求头
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
        }

        # 4. 组装请求体
        payload = {
            "model": settings.LLM_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个简洁、准确的中文助手。"
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            "stream": False,
            "temperature": 0.7,
            "thinking": {
                "type": "disabled"
            }
        }

        # 5. 发送 HTTP 请求
        try:
            with httpx.Client(timeout=settings.LLM_TIMEOUT) as client:
                response = client.post(url, headers=headers, json=payload)
                response.raise_for_status()

        except httpx.TimeoutException as e:
            raise LLMProviderError("大模型接口请求超时，请稍后重试") from e

        except httpx.HTTPStatusError as e:
            status_code = e.response.status_code
            detail = e.response.text[:300]
            raise LLMProviderError(
                f"大模型接口返回错误，状态码：{status_code}，响应内容：{detail}"
            ) from e

        except httpx.HTTPError as e:
            raise LLMProviderError(f"大模型接口请求失败：{str(e)}") from e

        # 6. 解析模型返回
        try:
            result = response.json()
            answer = result["choices"][0]["message"]["content"]
            return answer

        except (KeyError, IndexError, TypeError, ValueError) as e:
            raise LLMResponseParseError("大模型返回格式解析失败") from e