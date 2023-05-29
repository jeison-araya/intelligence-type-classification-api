from pydantic import BaseModel
from pydantic import Field
from app.database.schemas import BaseConfig
from app.database.schemas import PyObjectId


class _BaseQuestion(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    text: str

    class Config(BaseConfig):
        pass


class Question(_BaseQuestion):
    pass