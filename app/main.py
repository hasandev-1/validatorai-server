from app.routers.auth_routers import auth_router
from fastapi import FastAPI
from .routers import router
from .db.database  import engine , Base
from app.models import users
from app.routers.tts_routers import tts_router 

# creating the tables
app = FastAPI()

Base.metadata.create_all(bind = engine) # here we create all the tables

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI"}


app.include_router(router)   
app.include_router(auth_router)
app.include_router(tts_router)
