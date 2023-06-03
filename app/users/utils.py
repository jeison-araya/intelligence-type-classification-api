from datetime import datetime, timedelta
import jwt
from jwt.exceptions import ExpiredSignatureError
from jwt.exceptions import PyJWTError
from app.users.schemas import Token
from app.utility import utils

SECRET_KEY = utils.getenv('SECRET_KEY')


def generate_token(user_id: str) -> str:
    expiration_time = datetime.utcnow() + timedelta(minutes=60)

    payload = {
        "sub": user_id,
        "exp": expiration_time
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return Token(access_token=token, token_type="bearer")


def extract_user_id_from_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        expiration_time = payload.get('exp')

        if expiration_time is None:
            return False

        return payload.get('sub')

    except ExpiredSignatureError:
        return False
    except PyJWTError:
        raise False
