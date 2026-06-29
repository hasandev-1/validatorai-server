from pydantic import BaseModel

class testUser(BaseModel):
    username:str
    email:str
    password:str

    