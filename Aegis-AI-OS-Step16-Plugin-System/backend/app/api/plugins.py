from fastapi import APIRouter
from app.plugins.plugin_manager import list_plugins

router=APIRouter()

@router.get("/")
def plugins():
    return {"plugins":list_plugins()}
