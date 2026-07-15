from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
import os
DATABASE_URL=os.getenv("DATABASE_URL","sqlite:///./aegis.db")
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()
