from typing import List
from pydantic import BaseModel
from pydantic import Field
from app.database.schemas import BaseConfig
from app.database.schemas import PyObjectId


class Weight(BaseModel):
    intelligence_code: int
    weight: int = Field(..., ge=0, le=12)


class _BaseQuestion(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    question: str
    weights: List[Weight] = []

    class Config(BaseConfig):
        pass


class Question(_BaseQuestion):
    pass
