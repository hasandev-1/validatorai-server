from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
def user():
    return {"message": "Hello from user"}

@router.get("/login")
def login():
    return {"message": "Hello from login"}

