from bson import ObjectId
from pydantic import BaseModel
from pydantic import Field
from app.database.schemas import BaseConfig
from app.database.schemas import PyObjectId


class _BaseQuestion(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    text: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class Question(_BaseQuestion):
    pass
