from fastapi import APIRouter
from app.schemas.file import DirectoryRequest,FileRequest
from app.agents.file_agent import list_directory,read_text_file

router=APIRouter()

@router.post("/list")
def list_files(req:DirectoryRequest):
    return list_directory(req.path)

@router.post("/read")
def read_file(req:FileRequest):
    return read_text_file(req.path)
