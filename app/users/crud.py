"""
CRUD operations for users
"""
from bson import ObjectId
from app.users.schemas import UserDB
from app.users.schemas import CreateUser
from app.users.schemas import Token
from app.database.mongo import database
from app.users import utils
from fastapi import HTTPException


COLLECTON_NAME = 'users'


def get_user_by_id(user_id: str) -> UserDB:
    result = database[COLLECTON_NAME].find_one(ObjectId(user_id))

    return UserDB(**result) if result else None


def get_user_by_email(email: str) -> UserDB:
    result = database[COLLECTON_NAME].find_one({'email': email})

    return UserDB(**result) if result else None


def create_user(user: CreateUser) -> UserDB:
    result = database[COLLECTON_NAME].insert_one(user.dict())

    return User(**user.dict(), id=result.inserted_id)


def create_token(user: UserDB) -> Token:
    return utils.generate_token(str(user.id))


def get_user_by_token(token: str) -> UserDB:
    """
    Gets an user from a token
    """
    try:
        user_id = utils.extract_user_id_from_token(token)

        if not user_id:
            raise HTTPException(detail='Invalid token.', status_code=401)

        return get_user_by_id(user_id)

    except IndexError:
        raise HTTPException(detail='Invalid token.', status_code=401)
