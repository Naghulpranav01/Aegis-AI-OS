from fastapi import APIRouter,HTTPException
from app.schemas.auth import LoginRequest
from app.auth.security import hash_password,verify_password,create_access_token

router=APIRouter()

_fake={"admin":hash_password("admin123")}

@router.post("/login")
def login(data:LoginRequest):
    if data.username not in _fake or not verify_password(data.password,_fake[data.username]):
        raise HTTPException(status_code=401,detail="Invalid credentials")
    return {"access_token":create_access_token(data.username),"token_type":"bearer"}

@router.post("/register")
def register(data:LoginRequest):
    return {"message":"Registration placeholder","username":data.username}
