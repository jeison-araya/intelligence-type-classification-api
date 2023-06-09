from typing import List
from fastapi import HTTPException
from app.questions.schemas import QuestionDB
from app.answers.schemas import Answer
from app.intelligences_profiles.schemas import CreateIntelligenceProfile
from app.intelligences_profiles.schemas import IntelligenceProfileItem
from app.intelligences_profiles.schemas import IntelligenceProfile
from app.intelligences.crud import get_intelligences
from app.intelligences.schemas import IntelligenceDB
from app.questions import crud as questions_crud
from app.intelligences_profiles import crud as intelligences_profiles_crud

INTELLIGENCES: List[IntelligenceDB] = get_intelligences()
QUESTIONS: List[QuestionDB] = questions_crud.get_questions()


def generate_intelligence_profile_from_answers(user_id: str, answers: List[Answer]) -> IntelligenceProfile:
    intelligence_profile = CreateIntelligenceProfile(user_id=user_id)

    for intelligence in INTELLIGENCES:
        intelligence_profile_item = IntelligenceProfileItem(
            intelligence_code=intelligence.code, weight=0)

        for answer in answers:
            question = next(
                (question for question in QUESTIONS if str(question.id) == answer.question_id), None)
            question_weight = next(
                (question_weight for question_weight in question.weights if question_weight.intelligence_code == intelligence.code), None)

            intelligence_profile_item.weight += answer.weight * question_weight.weight

        intelligence_profile.items.append(intelligence_profile_item)

    intelligence_profile.sort_items_by_weight()

    return intelligences_profiles_crud.create_intelligence_profile(
        intelligence_profile=intelligence_profile)


def intelligence_profile_match(user_id: str):
    intelligence_profile = intelligences_profiles_crud.get_intelligence_profile_by_user_id(
        user_id=user_id)

    if not intelligence_profile:
        raise HTTPException(
            status_code=404, detail='Intelligence profile not found')

    similar_intelligence_profiles = []

    for intelligence_profile_db in intelligences_profiles_crud.get_intelligences_profiles():
        if intelligence_profile_db.user_id == user_id:
            continue

        distance = 0

        for item in intelligence_profile.items:
            item_db = next(
                (item_db for item_db in intelligence_profile_db.items if item_db.intelligence_code == item.intelligence_code), None)

            if item_db:
                distance += (item.weight - item_db.weight) ** 2

        similar_intelligence_profiles.append({
            'user_id': intelligence_profile_db.user_id,
            'distance': distance ** 0.5
        })

    return sorted(similar_intelligence_profiles, key=lambda item: item['distance'])
