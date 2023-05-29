from pydantic import BaseModel
from pydantic import Field
from app.database.schemas import PyObjectId
from app.database.schemas import BaseConfig


class Intelligence(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    name: str
    description: str

    class Config(BaseConfig):
        pass
