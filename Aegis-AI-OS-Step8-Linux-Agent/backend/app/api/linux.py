from fastapi import APIRouter
from app.schemas.linux import LinuxRequest
from app.agents.linux_agent import execute

router=APIRouter()

@router.post("/")
def run_linux(req:LinuxRequest):
    return execute(req.action)
