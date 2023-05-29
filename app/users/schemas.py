from pydantic import BaseModel
from pydantic import Field
from app.database.schemas import BaseConfig
from app.database.schemas import PyObjectId


class _BaseUser(BaseModel):
    email: str
    password: str
    full_name: str


class CreateUser(_BaseUser):
    class Config(BaseConfig):
        schema_extra = {
            'example': {
                'email': 'user@mail.com',
                'password': 'secret',
                'full_name': 'John Doe'
            }
        }


class User(_BaseUser):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')

    class Config(BaseConfig):
        pass


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCredentials(BaseModel):
    email: str
    password: str
