from pydantic import BaseModel
from pydantic import Field
from app.database.schemas import BaseConfig


class _BaseAnswer(BaseModel):
    question_id: str
    weight: int = Field(..., ge=0, le=10)

    class Config(BaseConfig):
        pass


class Answer(_BaseAnswer):
    pass
