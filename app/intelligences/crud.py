"""
CRUD operations for intelligences
"""
from app.intelligences.schemas import Intelligence
from app.database.mongo import database


COLLECTON_NAME = 'intelligences'


def get_intelligences() -> Intelligence:
    result = database[COLLECTON_NAME].find()

    return [Intelligence(**value) for value in result] if result else []
