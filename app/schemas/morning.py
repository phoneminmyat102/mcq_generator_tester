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
    text: Optional[str]
    option_a: Optional[str]
    option_b: Optional[str]
    option_c: Optional[str]
    option_d: Optional[str]
    type: Optional[QuestionTypeEnum]
    answer: Optional[AnswerEnum]