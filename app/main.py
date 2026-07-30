from fastapi import FastAPI
from app.agent import agent
from app.schemas.request import ChatRequest
from app.schemas.response import ChatResponse
from app.services.agent_service import chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Vet AI Assistant"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://vet-pals-clinic.lovable.app",
        "https://id-preview--ae1d4e9b-122a-4bd8-9264-b23ac7416bfb.lovable.app",
        "https://ae1d4e9b-122a-4bd8-9264-b23ac7416bfb.lovableproject.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post(
    "/chat",
    response_model=ChatResponse,
)
async def chatbot(request: ChatRequest):

    response = chat(request.message)

    return ChatResponse(
        response=response
    )