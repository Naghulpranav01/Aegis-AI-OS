from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from .database import Base
class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    username=Column(String,unique=True)
    password_hash=Column(String)
