"""
CRUD operations for questions
"""
import random
from typing import List
from app.questionnaires.questions.schemas import Question
from app.database.mongo import database


COLLECTON_NAME = 'questions'


def get_questions() -> List[Question]:
    result = database[COLLECTON_NAME].find()

    questions = [Question(**value) for value in result] if result else []

    random.shuffle(questions)

    return questions


def get_question(question_id: str) -> Question:
    result = database[COLLECTON_NAME].find_one({'_id': question_id})

    return Question(**result) if result else None