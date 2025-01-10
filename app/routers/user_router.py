from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from db.database import get_db
from models.user import User
from schemas.user import UserCreateModel, UserResponseModel, UserUpdateModel
from repositories.user_repo import UserRepository

router = APIRouter()

@router.post('/users/', response_model=UserResponseModel)
async def user_register(user: UserCreateModel, db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    registered_user = await repo.create(User(**user.model_dump()))
    return registered_user

@router.get('/users/', response_model=List[UserResponseModel])
async def list_users(db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    users = await repo.get_all()
    return users