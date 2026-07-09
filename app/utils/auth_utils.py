from datetime import timedelta
from datetime import timezone
from datetime import datetime
from passlib.context import CryptContext
from app.config import SECRET_KEY
from jose import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 7

ALGORITHM = "HS256"


  
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

# For verifying the Password

def verify_password(plain_password, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)

# Functionality to create the Access Token

def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode , SECRET_KEY, algorithm = ALGORITHM)

    return encoded_jwt

# Functionality to create the Refresh token 

def create_refresh_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode , SECRET_KEY, algorithm = ALGORITHM)

    return encoded_jwt