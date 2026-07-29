from langchain_openai import ChatOpenAI

from app.config import settings


llm = ChatOpenAI(
    model=settings.OPENROUTER_MODEL_NAME,
    api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    temperature=0,
)