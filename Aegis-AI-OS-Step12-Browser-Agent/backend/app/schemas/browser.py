from pydantic import BaseModel
class BrowserRequest(BaseModel):
    url:str
