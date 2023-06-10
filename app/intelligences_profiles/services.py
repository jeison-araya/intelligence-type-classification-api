from typing import List
from fastapi import HTTPException
from app.answers.schemas import Answer
from app.intelligences.crud import get_intelligences
from app.intelligences.schemas import IntelligenceDB
from app.intelligences_profiles.schemas import CreateIntelligenceProfile
from app.intelligences_profiles.schemas import IntelligenceProfileItem
from app.intelligences_profiles.schemas import IntelligenceProfile
from app.intelligences_profiles.schemas import IntelligenceProfileUser
from app.intelligences_profiles.schemas import IntelligenceProfileMatch
from app.intelligences_profiles.schemas import IntelligenceProfileMatchUser
from app.intelligences_profiles import crud as intelligences_profiles_crud
from app.questions import crud as questions_crud
from app.questions.schemas import QuestionDB
from app.users.crud import get_user_by_id


INTELLIGENCES: List[IntelligenceDB] = get_intelligences()
QUESTIONS: List[QuestionDB] = questions_crud.get_questions()


def generate_intelligence_profile_from_answers(user_id: str, answers: List[Answer]) -> IntelligenceProfile:
    user_db = get_user_by_id(user_id=user_id)

    if (not user_db):
        raise HTTPException(status_code=404, detail='User not found')

    intelligence_profile = CreateIntelligenceProfile(
        user=IntelligenceProfileUser(
            user_id=user_db.id,
            full_name=user_db.full_name,
            email=user_db.email
        )
    )

    for intelligence in INTELLIGENCES:
        intelligence_profile_item = IntelligenceProfileItem(
            intelligence_code=intelligence.code,
            intelligence_name=intelligence.name,
            weight=0
        )

        for answer in answers:
            question = next(
                (question for question in QUESTIONS if str(question.id) == answer.question_id), None)
            question_weight = next(
                (question_weight for question_weight in question.weights if question_weight.intelligence_code == intelligence.code), None)

            intelligence_profile_item.weight += answer.weight * question_weight.weight

        intelligence_profile.items.append(intelligence_profile_item)

    intelligence_profile.sort_items_by_weight()

    return intelligence_profile


def intelligence_profile_match(user_id: str):
    intelligence_profile = intelligences_profiles_crud.get_intelligence_profile_by_user_id(
        user_id=user_id)

    if not intelligence_profile:
        raise HTTPException(
            status_code=404, detail='Intelligence profile not found')

    intelligence_profiles_matches = []

    for intelligence_profile_db in intelligences_profiles_crud.get_intelligences_profiles():
        if str(intelligence_profile_db.user.user_id) == user_id:
            continue

        distance = 0

        for item in intelligence_profile.items:
            item_db = next(
                (item_db for item_db in intelligence_profile_db.items if item_db.intelligence_code == item.intelligence_code), None)

            if item_db:
                distance += (item.weight - item_db.weight) ** 2

        intelligence_profiles_matches.append(
            IntelligenceProfileMatch(
                user=IntelligenceProfileMatchUser(
                    **intelligence_profile_db.user.dict()),
                distance=distance ** 0.5
            ))

    if len(intelligence_profiles_matches) == 0:
        return []

    intelligence_profiles_matches.sort(key=lambda match: match.distance)

    return intelligence_profiles_matches
