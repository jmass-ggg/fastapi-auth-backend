from pydantic import BaseModel,EmailStr
from uuid import UUID
class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserRead(BaseModel):
    id:int
    email:EmailStr
    class Config:
        orm_mode=True
class UserLogin(BaseModel):   # <-- Add this schema
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token:str
    token_type:str
    