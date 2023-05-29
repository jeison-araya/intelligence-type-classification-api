"""
Questions router
"""
from typing import List

from fastapi import APIRouter
from app.questions import crud
from app.questions.schemas import Question


router = APIRouter()


@router.get('/questions/', response_model=List[Question])
def get_questions():
    return crud.get_questions()
