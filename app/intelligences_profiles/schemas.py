from pydantic import Field
from pydantic import BaseModel
from app.database.schemas import BaseConfig
from app.database.schemas import PyObjectId


class _BaseIntelligenceProfileItem(BaseModel):
    intelligence_code: int
    weight: int

    class Config(BaseConfig):
        pass


class IntelligenceProfileItem(_BaseIntelligenceProfileItem):
    pass


class _BaseIntelligenceProfile(BaseModel):
    user_id: str
    items: list[IntelligenceProfileItem] = []

    def sort_items_by_weight(self, assending: bool = True):
        self.items = sorted(
            self.items, key=lambda item: item.weight, reverse=assending)

    class Config(BaseConfig):
        pass


class CreateIntelligenceProfile(_BaseIntelligenceProfile):
    pass


class UpdateIntelligenceProfile(_BaseIntelligenceProfile):
    pass


class IntelligenceProfile(_BaseIntelligenceProfile):
    pass


class IntelligenceProfileDB(_BaseIntelligenceProfile):
    pass
