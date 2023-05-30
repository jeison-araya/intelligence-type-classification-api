from pydantic import BaseModel
from pydantic import Field
from app.database.schemas import BaseConfig
from app.database.schemas import PyObjectId


class Answer(BaseModel):
    question_id: PyObjectId = Field(default_factory=PyObjectId)
    weight: int = Field(..., ge=0, le=10)

    class Config(BaseConfig):
        pass
