from fastapi import APIRouter
router=APIRouter()
@router.get("/")
def get_settings(): return {"theme":"dark"}
@router.post("/")
def save_settings(settings:dict): return {"saved":settings}