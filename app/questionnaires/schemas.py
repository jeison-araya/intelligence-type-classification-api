from typing import List
from pydantic import BaseModel
from pydantic import Field
from app.database.schemas import BaseConfig
from app.database.schemas import PyObjectId
from app.questionnaires.questions.schemas import Question


class Questionnaire(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    name: str
    description: str
    questions: List[Question] = []

    class Config(BaseConfig):
        pass
