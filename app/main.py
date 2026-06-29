from fastapi import FastAPI
from .routers import router
from .db.database  import engine 

# creating the tables


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI"}

app.include_router(router)   

