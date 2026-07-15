from fastapi import APIRouter
from app.schemas.terminal import TerminalRequest
from app.agents.terminal_agent import execute

router=APIRouter()

@router.post("/")
def terminal(req:TerminalRequest):
    return execute(req.command)
