from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from db.database import get_db
from models.user import User
from schemas.user import UserCreateModel, UserResponseModel, UserUpdateModel, UserLoginModel
from repositories.user_repo import UserRepository
from auth import create_access_token, get_current_user

router = APIRouter()


@router.post("/register", response_model=UserResponseModel)
async def register_user(user: UserCreateModel, db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    existing_user = await repo.get_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await repo.register_user(User(**user.model_dump()))
    return new_user

@router.post("/login")
async def login_user(user_credentials: UserLoginModel, db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    user = await repo.authenticate_user(user_credentials.email, user_credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

@router.get('/users/', response_model=List[UserResponseModel])
async def list_users(db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    users = await repo.get_all()
    return users