from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy import update, delete
from typing import List, Optional
from models.user import User
from auth import verify_password, get_password_hashed
class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User) -> User:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_by_id(self, question_id: int) -> Optional[User]:
        result = await self.session.execute(select(User).where(User.id == question_id))
        return result.scalar_one_or_none()
    
    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def get_all(self) -> List[User]:
        result = await self.session.execute(select(User))
        return result.scalars().all()

    async def update(self, user_id: int, **kwargs) -> Optional[User]:
        query = update(User).where(User.id == user_id).values(**kwargs).execution_options(synchronize_session="fetch")
        await self.session.execute(query)
        await self.session.commit()
        return await self.get_by_id(user_id)

    async def delete(self, user_id: int) -> bool:
        query = delete(User).where(User.id == user_id)
        result = await self.session.execute(query)
        await self.session.commit()
        return result.rowcount > 0
    
    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        result = await self.session.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()
        if user and verify_password(password, user.password):
            return user
        return None

    async def register_user(self, user: User) -> User:
        user.password = get_password_hashed(user.password)
        return await self.create(user)