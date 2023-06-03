from typing import List
from pydantic import BaseModel
from app.database.schemas import BaseConfig
from app.intelligences.schemas import Intelligence


class Questionnaire(BaseModel):
    name: str
    description: str
    intelligences: List[Intelligence] = []

    class Config(BaseConfig):
        pass
