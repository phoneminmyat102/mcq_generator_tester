from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from db.database import get_db
from models.morning import Morning
from schemas.morning import MorningCreateModel, MorningResponseModel, MorningUpdateModel
from repositories.morning_repo import MorningRepository

router = APIRouter()

@router.get("/morning/random", response_model=List[MorningResponseModel])
async def get_random_morning_questions(db: AsyncSession = Depends(get_db)):
    repo = MorningRepository(db)
    questions = await repo.get_random_questions(count_per_type=2)
    return questions

@router.post('/morning/', response_model=MorningResponseModel)
async def create_morning_question(morning:MorningCreateModel, db: AsyncSession = Depends(get_db)):
    repo = MorningRepository(db)
    new_question = await repo.create(Morning(**morning.model_dump()))
    return new_question

@router.get('/morning/{question_id}', response_model=MorningResponseModel)
async def get_morning_question(question_id: int, db: AsyncSession = Depends(get_db)):
    repo = MorningRepository(db)
    question = await repo.get_by_id(question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question Not Found!")
    return question

@router.get('/morning/', response_model=List[MorningResponseModel])
async def list_morning_questions(db: AsyncSession = Depends(get_db)):
    repo = MorningRepository(db)
    questions = await repo.get_all()
    return questions

@router.post('/morning/{question_id}/update', response_model=MorningResponseModel)
async def update_morning_question(question_id: int, morning: MorningUpdateModel, db: AsyncSession = Depends(get_db)):
    repo = MorningRepository(db)
    updated_question = await repo.update(question_id, **morning.model_dump(exclude_unset=True))
    if not updated_question:
        raise HTTPException(status_code=404, detail="Question Not Found!")
    return updated_question

@router.delete('/morning/{question_id}/delete')
async def delete_morning_question(question_id: int, db: AsyncSession = Depends(get_db)):
    repo = MorningRepository(db)
    result = await repo.delete(question_id)
    if not result:
        raise HTTPException(status_code=404, detail="Question Not Found!")
    return {"message": "Question deleted successfully"}