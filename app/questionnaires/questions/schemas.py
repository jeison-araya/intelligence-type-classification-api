from typing import List
from pydantic import BaseModel
from pydantic import Field
from app.database.schemas import BaseConfig
from app.database.schemas import PyObjectId


class Weight(BaseModel):
    intelligence_id: PyObjectId = Field(default_factory=PyObjectId)
    weight: int = Field(..., ge=0, le=10)


class _BaseQuestion(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    question: str

    class Config(BaseConfig):
        pass


class Question(_BaseQuestion):
    pass


class QuestionInBD(_BaseQuestion):
    weights: List[Weight] = []