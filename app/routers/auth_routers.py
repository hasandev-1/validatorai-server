from sqlalchemy.orm import Session
from app.utils.auth_utils import hash_password, verify_password
from fastapi import APIRouter , Depends, status , HTTPException
from app.schemas.user import UserSignup , UserLogin
from app.models.users import User
from app.db.database import get_db


auth_router = APIRouter(prefix="/auth")

@auth_router.post('/signup')
def signup(user:UserSignup, db: Session = Depends(get_db)):
    #We need to check if the user is already exist
    
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "Email already registered"
        )

    
    # we need to hash the password
    hashed_password = hash_password(user.password)

    new_user =  User(
        username = user.username ,  
        email = user.email,
        password_hash = hashed_password
        )
    
    # we need to add the user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"User signedUp successfully", "user":new_user}
@auth_router.post('/login')
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user_credentials.email).first()
    
    if not db_user or not verify_password(user_credentials.password, db_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    return {
        "message": "Login successfully", 
        "user": {
            "username": db_user.username,
            "email": db_user.email
        }
    }