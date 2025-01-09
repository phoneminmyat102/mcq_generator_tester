from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy import update, delete
from typing import List, Optional
from sqlalchemy.sql.expression import func
from models.morning import Morning

class MorningRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, morning: Morning) -> Morning:
        """Add a new morning question to the database."""
        self.session.add(morning)
        await self.session.commit()
        await self.session.refresh(morning)
        return morning

    async def get_by_id(self, question_id: int) -> Optional[Morning]:
        """Retrieve a morning question by its ID."""
        result = await self.session.execute(select(Morning).where(Morning.id == question_id))
        return result.scalar_one_or_none()

    async def get_all(self) -> List[Morning]:
        """Retrieve all morning questions."""
        result = await self.session.execute(select(Morning))
        return result.scalars().all()

    async def update(self, question_id: int, **kwargs) -> Optional[Morning]:
        """Update an existing morning question."""
        query = update(Morning).where(Morning.id == question_id).values(**kwargs).execution_options(synchronize_session="fetch")
        await self.session.execute(query)
        await self.session.commit()
        return await self.get_by_id(question_id)

    async def delete(self, question_id: int) -> bool:
        """Delete a morning question by its ID."""
        query = delete(Morning).where(Morning.id == question_id)
        result = await self.session.execute(query)
        await self.session.commit()
        return result.rowcount > 0
    
    async def get_random_questions(self, count_per_type: int = 2) -> List[Morning]:
        result = []
        # Loop through each type and get `count_per_type` random questions
        for question_type in ['1', '2', '3']:
            stmt = (
                select(Morning)
                .where(Morning.type == question_type)
                .order_by(func.rand())  # For MySQL
                .limit(count_per_type)
            )
            query_result = await self.session.execute(stmt)
            questions = query_result.scalars().all()
            result.extend(questions)
        return result
