from fastapi import APIRouter
from app.schemas.memory import MemoryRequest
from app.services.memory_service import save_memory,get_memories

router=APIRouter()

@router.post("/")
def add_memory(req:MemoryRequest):
    save_memory(req.text)
    return {"status":"saved"}

@router.get("/")
def list_memory():
    return {"memories":get_memories()}
