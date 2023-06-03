from pydantic import BaseModel
from pydantic import Field
from app.database.schemas import BaseConfig
from app.database.schemas import PyObjectId


class _BaseUser(BaseModel):
    email: str
    full_name: str

    class Config(BaseConfig):
        pass


class CreateUser(_BaseUser):
    password: str


class User(_BaseUser):
    pass


class UserDB(_BaseUser):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class Login(BaseModel):
    email: str
    password: str
