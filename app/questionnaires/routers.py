"""
Questionnaires router
"""
from fastapi import APIRouter

from app.questionnaires.questions.routers import router as questions_router
from app.questionnaires.responses.routers import router as responses_router

router = APIRouter(prefix='/questionnaires', tags=['Questionnaires'])

router.include_router(questions_router)
router.include_router(responses_router)
