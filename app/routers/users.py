from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
def user():
    return {"message": "Hello from user"}

    