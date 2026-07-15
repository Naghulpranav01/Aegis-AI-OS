from fastapi import APIRouter
from app.schemas.document import DocumentRequest
from app.services.document_service import summarize

router=APIRouter()

@router.post("/summarize")
def summarize_doc(req:DocumentRequest):
    return summarize(req.path)
