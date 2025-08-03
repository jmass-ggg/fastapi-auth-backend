from sqlalchemy import Column,String,Integer
from app.database import Base

class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True, index=True)
    email=Column(String,nullable=False,unique=True)
    hashed_password=Column(String,nullable=False)
