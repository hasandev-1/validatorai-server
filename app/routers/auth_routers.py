from app.utils.auth_utils import create_refresh_token
from app.utils.auth_utils import create_access_token
from sqlalchemy.orm import Session
from app.utils.auth_utils import hash_password, verify_password
from fastapi import APIRouter , Depends, status , HTTPException , Response , Request
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
def login(response: Response , user_credentials: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user_credentials.email).first()
    
    if not db_user or not verify_password(user_credentials.password, db_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )


    # We need to create the access token 

    access_token = create_access_token(data = {"userId": db_user.id})

    # we need to create the refresh token 

    refresh_token = create_refresh_token(data = {"userId": db_user.id})

    # we need to set the refresh token in the response cookie

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,            # Prevents JavaScript reading the cookie (XSS protection)
        secure=False,             # Set to False for local HTTP development (True in production)
        samesite="lax",           # Protects against CSRF attacks
        max_age=60 * 60 * 24 * 7, # Cookie expires in 7 days (in seconds)
        path="/"                  # Set path to root so it matches all routes
    )

    # Remove Password before sending response 

    user_data = {
        "user_id" : db_user.id,
        "email" : db_user.email,
        "username" : db_user.username
    }

    db_user.password_hash = ""

    return {
        "message": "Login successfully", 
        "data":{
            "user" : db_user,
            "access_token" : access_token,
        } ,
        "status_code": status.HTTP_200_OK
    }

    