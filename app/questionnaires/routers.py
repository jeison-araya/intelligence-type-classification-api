"""
Questionnaires router
"""
from fastapi import APIRouter

from app.questionnaires.questions.routers import router as questions_router
from app.questionnaires.actions.routers import router as actions_router

router = APIRouter(prefix='/questionnaires', tags=['Questionnaires'])

router.include_router(questions_router)
router.include_router(actions_router)
