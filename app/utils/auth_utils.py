from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

# For verifying the Password

def verify_password(plain_password, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)