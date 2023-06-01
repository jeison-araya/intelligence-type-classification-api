from typing import List
from app.questionnaires.answers.schemas import Answer
from app.questionnaires.actions.schemas import IntelligenceProfile
from app.questionnaires.questions import crud as questions_crud
from app.intelligences.schemas import Intelligence
from app.questionnaires.actions.utils import sort_by_weight


def get_intelligence_profiles(answers: List[Answer], intelligences: List[Intelligence]):
    intelligence_profiles = []

    for intelligence in intelligences:
        intelligence_profile = IntelligenceProfile(intelligence.id)
        for answer in answers:    
            question = questions_crud.get_question(answer.question_id)
            for question_weight in question.weights:
                if question_weight.intelligence_id == intelligence.id:
                    intelligence_profile.weight += answer.weight * question_weight.weight
            
        intelligence_profiles.append(intelligence_profile)

    return sort_by_weight(intelligence_profiles)
