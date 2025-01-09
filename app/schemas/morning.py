from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum

class QuestionTypeEnum(str, Enum):
    part1 = "1"
    part2 = "2"
    part3 = "3"

class AnswerEnum(str, Enum):
    option_a = "a"
    option_b = "b"
    option_c = "c"
    option_d = "d"

class MorningResponseModel(BaseModel):
    id: int
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    type: QuestionTypeEnum
    answer: AnswerEnum

    model_config = ConfigDict(from_attributes=True)
    
class MorningCreateModel(BaseModel):
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    type: QuestionTypeEnum
    answer: AnswerEnum

class MorningUpdateModel(BaseModel):
    text: Optional[str] = None
    option_a: Optional[str] = None
    option_b: Optional[str] = None
    option_c: Optional[str] = None
    option_d: Optional[str] = None
    type: Optional[QuestionTypeEnum] = None
    answer: Optional[AnswerEnum] = None