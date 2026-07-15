from datetime import datetime,timedelta
from jose import jwt
from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
SECRET_KEY="CHANGE_ME"
ALGORITHM="HS256"

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(password:str,hashed:str)->bool:
    return pwd_context.verify(password,hashed)

def create_access_token(subject:str,minutes:int=60):
    payload={"sub":subject,"exp":datetime.utcnow()+timedelta(minutes=minutes)}
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
