from fastapi import APIRouter
router=APIRouter()
@router.get("/")
def status(): return {"backend":"online","version":"0.1.0"}