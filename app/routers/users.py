from app.schemas.test import testUser
from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
def user():
    return {"message": "Hello from user"}

@router.get("/login")
def login():
    return {"message": "Hello from login"}

@router.post("/signup")
def signup(user:testUser):
    return {"name":user.username, "email":user.email, "password":user.password, "message":"User signedUp"}

    