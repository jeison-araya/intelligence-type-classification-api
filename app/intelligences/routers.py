"""
Intelligences router
"""
from typing import List
from fastapi import APIRouter
from app.intelligences import crud
from app.intelligences.schemas import Intelligence


router = APIRouter()


@router.get('/intelligences/', response_model=List[Intelligence])
def get_intelligences():
    return crud.get_intelligences()
