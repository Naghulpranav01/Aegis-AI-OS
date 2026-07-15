from fastapi import APIRouter
from app.schemas.voice import SpeakRequest
from app.services.voice_service import transcribe_placeholder,speak_placeholder

router=APIRouter()

@router.get("/listen")
def listen():
    return transcribe_placeholder()

@router.post("/speak")
def speak(req:SpeakRequest):
    return speak_placeholder(req.text)
