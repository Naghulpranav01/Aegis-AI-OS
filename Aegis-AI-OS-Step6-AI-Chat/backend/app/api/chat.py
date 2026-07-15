from fastapi import APIRouter
from app.schemas.chat import ChatRequest
from app.services.ollama_service import chat

router=APIRouter()

@router.post("/")
def chat_endpoint(req:ChatRequest):
    return {"response":chat(req.message)}
