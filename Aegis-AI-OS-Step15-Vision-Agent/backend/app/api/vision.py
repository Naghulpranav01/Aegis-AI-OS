from fastapi import APIRouter
from app.schemas.vision import VisionRequest
from app.services.vision_service import analyze_image

router=APIRouter()

@router.post("/analyze")
def analyze(req:VisionRequest):
    return analyze_image(req.path)
