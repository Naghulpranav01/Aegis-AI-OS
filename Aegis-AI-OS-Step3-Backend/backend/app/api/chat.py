from fastapi import APIRouter
router=APIRouter()
@router.post("/")
def chat(message:dict): return {"reply":"AI integration coming in Step 5","echo":message}