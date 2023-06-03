from typing import List
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
