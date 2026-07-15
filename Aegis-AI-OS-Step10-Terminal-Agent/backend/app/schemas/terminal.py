from pydantic import BaseModel
class TerminalRequest(BaseModel):
    command:str
