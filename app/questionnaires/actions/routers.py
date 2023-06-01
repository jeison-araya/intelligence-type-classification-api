"""
Questions router
"""
from fastapi import APIRouter
from app.questionnaires.actions.schemas import Submit
from app.questionnaires.actions import services as actions_services
from app.intelligences.crud import get_intelligences

router = APIRouter()
intelligences = get_intelligences()

@router.put('/actions/submit/')
def submit_questionnaire(submit: Submit):
    return actions_services.get_intelligence_profiles(submit.answers, intelligences)
