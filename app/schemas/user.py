from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from enum import Enum


class UserResponseModel(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
    
class UserCreateModel(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserUpdateModel(BaseModel):
    pass