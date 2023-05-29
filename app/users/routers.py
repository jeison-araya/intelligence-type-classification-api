"""
Router for users
"""
from fastapi import APIRouter
from fastapi import HTTPException
from app.users import crud
from app.users.schemas import CreateUser
from app.users.schemas import User
from app.users.schemas import Token
from app.users.schemas import UserCredentials
from fastapi import Depends
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()


@router.post('/users/register/', response_model=User, status_code=201)
def register_user(user: CreateUser):
    if crud.get_user_by_email(user.email):
        raise HTTPException(
            detail='Email already registered.', status_code=400)

    return crud.create_user(user)


@router.post('/users/login/', response_model=Token)
def login_user(user_credentials: UserCredentials):
    user = crud.get_user_by_email(user_credentials.email)

    if not user:
        raise HTTPException(detail='User not found.', status_code=404)

    if not user_credentials.password == user.password:
        raise HTTPException(detail='Incorrect password.', status_code=400)

    return crud.create_token(user)


@router.get('/users/me/', response_model=User)
def get_user_me(credentials: HTTPAuthorizationCredentials = Depends(security)):
    user = crud.get_user_by_token(credentials.credentials)

    if not user:
        raise HTTPException(detail='User not found.', status_code=404)

    return user
