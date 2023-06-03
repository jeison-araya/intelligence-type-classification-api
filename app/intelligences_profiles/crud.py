from app.database.mongo import database
from bson.objectid import ObjectId
from app.intelligences_profiles.schemas import IntelligenceProfile
from app.intelligences_profiles.schemas import IntelligenceProfileDB
from app.intelligences_profiles.schemas import CreateIntelligenceProfile
from app.intelligences_profiles.schemas import UpdateIntelligenceProfile
COLLECTION_NAME = 'intelligences_profiles'


def create_intelligence_profile(intelligence_profile: CreateIntelligenceProfile) -> IntelligenceProfile:
    if get_intelligence_profile_by_user_id(intelligence_profile.user_id):
        update_intelligence_profile(intelligence_profile)

    else:
        database[COLLECTION_NAME].insert_one(intelligence_profile.dict())

    return get_intelligence_profile_by_user_id(intelligence_profile.user_id)
    

def update_intelligence_profile(intelligence_profile: UpdateIntelligenceProfile):
    database[COLLECTION_NAME].update_one(
        {'user_id': intelligence_profile.user_id},
        {'$set': intelligence_profile.dict()},
        upsert=True
    )

def get_intelligence_profile_by_user_id(user_id: str) -> IntelligenceProfileDB:
    result = database[COLLECTION_NAME].find_one({'user_id': user_id})

    return IntelligenceProfileDB(**result) if result else None
