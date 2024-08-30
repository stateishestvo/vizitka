from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    password: str
    phone_number: Optional[str] = None
    created_at: Optional[datetime] = None

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    status: Optional[str] = None
    role: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    username: str
    full_name: str
    email: EmailStr
    phone_number: Optional[str] = None
    status: str
    role: str
    created_at: datetime

    class Config:
        orm_mode = True