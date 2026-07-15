from pydantic import BaseModel
class Plugin(BaseModel):
    name:str
    version:str
    enabled:bool=True
