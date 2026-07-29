from fastapi import FastAPI
from app.agent import agent
from app.schemas.request import ChatRequest
from app.schemas.response import ChatResponse

app = FastAPI(
    title="Vet AI Assistant"
)

@app.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(request: ChatRequest):

    result = agent.invoke(
        {
            "message": [
                {
                    "role": "user",
                    "content": request.message,
                }
            ]
        }
    )

    return ChatResponse(
        response=result["message"][-1].content
    )