"""
Questions router
"""
from fastapi import APIRouter
from app.questionnaires.responses.schemas import Response

router = APIRouter()


@router.post('/responses/')
def create_response(response: Response):
    return 'response created'
