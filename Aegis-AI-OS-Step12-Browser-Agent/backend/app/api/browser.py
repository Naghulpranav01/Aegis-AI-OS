from fastapi import APIRouter
from app.schemas.browser import BrowserRequest
from app.services.browser_service import open_url
router=APIRouter()
@router.post("/open")
def open_browser(req:BrowserRequest):
    return open_url(req.url)
