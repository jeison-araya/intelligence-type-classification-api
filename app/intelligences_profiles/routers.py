from typing import List
from fastapi import APIRouter
from fastapi import HTTPException
from app.users import crud
from fastapi import Depends
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from app.intelligences_profiles import services as intelligences_profiles_services
from app.intelligences_profiles.schemas import IntelligenceProfile
from app.intelligences_profiles import crud as intelligences_profiles_crud


router = APIRouter()
security = HTTPBearer()


@router.get('/intelligences_profiles/', response_model=IntelligenceProfile)
def get_intelligences_profiles(credentials: HTTPAuthorizationCredentials = Depends(security)):
    user = crud.get_user_by_token(token=credentials.credentials)

    if not user:
        raise HTTPException(detail='User not found.', status_code=404)

    return intelligences_profiles_crud.get_intelligence_profile_by_user_id(user_id=str(user.id))


@router.get('/intelligences_profiles/actions/matches/', response_model=List)
def user_match(credentials: HTTPAuthorizationCredentials = Depends(security)):
    user = crud.get_user_by_token(token=credentials.credentials)

    if not user:
        raise HTTPException(detail='User not found.', status_code=404)

    return intelligences_profiles_services.intelligence_profile_match(user_id=str(user.id))
