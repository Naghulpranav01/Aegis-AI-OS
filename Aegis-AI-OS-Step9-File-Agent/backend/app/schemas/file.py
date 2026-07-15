from pydantic import BaseModel

class DirectoryRequest(BaseModel):
    path:str="."

class FileRequest(BaseModel):
    path:str
