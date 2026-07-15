from fastapi import APIRouter
from app.schemas.orchestrator import TaskRequest
from app.agents.orchestrator import orchestrator

router=APIRouter()

@router.post("/dispatch")
def dispatch(req:TaskRequest):
    return orchestrator.dispatch(req.task)
