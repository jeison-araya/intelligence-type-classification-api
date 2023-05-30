from typing import List
from pydantic import BaseModel
from app.database.schemas import BaseConfig

class IntelligenceProfile(BaseModel):
    intelligence_id: int
    weight: int

    class Config(BaseConfig):
        pass


class Profile(BaseModel):
    intelligences_types: List[IntelligenceProfile] = []

    class Config(BaseConfig):
        pass
