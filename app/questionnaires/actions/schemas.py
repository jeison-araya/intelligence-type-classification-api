from typing import List
from pydantic import BaseModel
from pydantic import Field
from app.database.schemas import BaseConfig
from app.database.schemas import PyObjectId
from app.questionnaires.answers.schemas import Answer


class Submit(BaseModel):
    user_id: PyObjectId = Field(default_factory=PyObjectId)
    answers: List[Answer]

    class Config(BaseConfig):
        pass



class IntelligenceProfile(BaseModel):
    intelligence_id: int
    weight: int

    class Config(BaseConfig):
        pass