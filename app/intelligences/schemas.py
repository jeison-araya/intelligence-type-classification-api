from pydantic import BaseModel
from app.database.schemas import BaseConfig


class _BaseIntelligence(BaseModel):
    name: str
    description: str

    class Config(BaseConfig):
        pass


class Intelligence(_BaseIntelligence):
    pass


class IntelligenceDB(_BaseIntelligence):
    code: int
