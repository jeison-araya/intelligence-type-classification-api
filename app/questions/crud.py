"""
CRUD operations for questions
"""
from app.questions.schemas import Question
from app.database.mongo import database


COLLECTON_NAME = 'questions'


def get_questions() -> Question:
    result = database[COLLECTON_NAME].find()

    return [Question(**value) for value in result] if result else []
