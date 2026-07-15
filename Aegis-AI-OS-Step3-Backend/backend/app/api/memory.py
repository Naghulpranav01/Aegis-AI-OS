from fastapi import APIRouter
router=APIRouter()
@router.get("/")
def memory(): return {"memories":[]}