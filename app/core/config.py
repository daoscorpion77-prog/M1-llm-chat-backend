import os
from dotenv import load_dotenv

# 读取 .env 文件
load_dotenv()


class Settings:
    # LLM 基础配置
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "")
    LLM_MODEL = os.getenv("LLM_MODEL", "")

    # DeepSeek 配置
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
    DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "")

    # 请求超时时间
    LLM_TIMEOUT = int(os.getenv("LLM_TIMEOUT", 30))

settings = Settings()