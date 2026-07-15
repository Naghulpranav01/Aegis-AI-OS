from typing import List
from datetime import datetime

class MemoryStore:
    def __init__(self):
        self.memories=[]
    def add(self,text:str):
        self.memories.append({"text":text,"created_at":datetime.utcnow().isoformat()})
    def all(self)->List[dict]:
        return self.memories

store=MemoryStore()
