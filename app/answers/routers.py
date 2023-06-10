from typing import List
from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from app.intelligences_profiles.services import generate_intelligence_profile_from_answers
from app.answers.schemas import Answer
from app.intelligences_profiles.schemas import IntelligenceProfile
from app.users.crud import get_user_by_token
from app.intelligences_profiles import crud as intelligences_profiles_crud


router = APIRouter()
security = HTTPBearer()


@router.put('/actions/submit/', response_model=IntelligenceProfile)
def save_answers(answers: List[Answer], credentials: HTTPAuthorizationCredentials = Depends(security)):
    user = get_user_by_token(token=credentials.credentials)

    intelligence_profile = generate_intelligence_profile_from_answers(
        user_id=str(user.id), answers=answers)

    intelligence_profile_db = intelligences_profiles_crud.create_intelligence_profile(
        intelligence_profile=intelligence_profile)

    return intelligence_profile_db
