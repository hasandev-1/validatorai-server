from pydantic import BaseModel, EmailStr, Field


class UserSignup(BaseModel):
    username:str
    email:EmailStr
    password:str
