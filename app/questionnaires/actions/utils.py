
from typing import List
from app.questionnaires.actions.schemas import IntelligenceProfile

def sort_by_weight(intelligence_profiles: List[IntelligenceProfile], assending: bool = False):
    return sorted(intelligence_profiles, key=lambda intelligence_profile: intelligence_profile.weight, reverse=assending)