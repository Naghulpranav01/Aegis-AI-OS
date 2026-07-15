from pydantic import BaseModel
class SpeakRequest(BaseModel):
    text:str
