from typing import List
from pydantic import BaseModel
from pydantic import Field
from app.database.schemas import BaseConfig
from app.database.schemas import PyObjectId
from app.questionnaires.answers.schemas import Answer


class Response(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')

    user_id: PyObjectId = Field(default_factory=PyObjectId)
    answers: List[Answer]

    class Config(BaseConfig):
        pass
