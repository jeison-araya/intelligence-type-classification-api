"""
CRUD operations for questions
"""
import random
from app.questions.schemas import Question
from app.database.mongo import database


COLLECTON_NAME = 'questions'


def get_questions() -> Question:
    result = database[COLLECTON_NAME].find()

    questions = [Question(**value) for value in result] if result else []

    random.shuffle(questions)

    return questions

