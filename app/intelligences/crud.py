"""
CRUD operations for intelligences
"""
from typing import List
from app.intelligences.schemas import IntelligenceDB
from app.database.mongo import database


COLLECTON_NAME = 'intelligences'


def get_intelligences() -> List[IntelligenceDB]:
    result = database[COLLECTON_NAME].find()

    return [IntelligenceDB(**value) for value in result] if result else []
