import os
from dotenv import load_dotenv

# 读取 .env 文件
load_dotenv()


class Settings:
    # LLM 配置
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "deepseek")
    LLM_MODEL = os.getenv("LLM_MODEL", "deepseek-chat")
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")


settings = Settings()