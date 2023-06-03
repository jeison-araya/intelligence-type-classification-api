"""
CRUD operations for questions
"""
import random
from typing import List
from app.questions.schemas import QuestionDB
from app.database.mongo import database


COLLECTION_NAME = 'questions'


def get_questions() -> List[QuestionDB]:
    result = database[COLLECTION_NAME].find()

    questions = [QuestionDB(**value) for value in result] if result else []

    random.shuffle(questions)

    return questions


def get_question(question_id: str) -> QuestionDB:
    result = database[COLLECTION_NAME].find_one({'_id': question_id})

    return QuestionDB(**result) if result else None