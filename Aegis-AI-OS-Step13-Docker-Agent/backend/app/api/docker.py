from fastapi import APIRouter
from app.services.docker_service import docker_info,list_containers

router=APIRouter()

@router.get("/info")
def info():
    return docker_info()

@router.get("/containers")
def containers():
    return list_containers()
