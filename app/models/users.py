from sqlalchemy import Column, String, Integer 
from app.db.database import Base
import uuid

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key = True, default = lambda: str(uuid.uuid4())) 
    username = Column(String, unique = True , index = True)
    email = Column(String, unique = True , index = True)
    password_hash = Column(String, nullable = True )


    