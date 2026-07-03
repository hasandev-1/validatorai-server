from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy import create_engine
from app.config import DATABASE_URL
from sqlalchemy.ext.declarative import declarative_base

# creating a database engine 

engine = create_engine(DATABASE_URL)
Base = declarative_base()

# we need to create a local session between the app and database

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency Function that gives us the db session for connecting 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# metadata is used to create the tables
try:
    connection = engine.connect()
    print("Database connection has been established")

    # Retreiving the version of postgresql
    result = connection.execute(text("SELECT version()"))
    db_version = result.scalar()
    print(f"Postgresql version : {db_version}")  

    connection.close()
except Exception:
    print("Failed to connect the database")


