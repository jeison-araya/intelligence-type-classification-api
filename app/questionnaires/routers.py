"""
Questionnaires router
"""
from fastapi import APIRouter
from app.questionnaires.actions.routers import router as actions_router

router = APIRouter(prefix='/questionnaires', tags=['Questionnaires'])

router.include_router(actions_router)
