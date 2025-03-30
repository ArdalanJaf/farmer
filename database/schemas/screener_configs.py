from pydantic import BaseModel
from typing import Optional, Dict

# ScreenerConfig CRUD-ops DTOs
class ScreenerConfigBase(BaseModel):
    name: str
    version: int
    config_json: Dict
    description: Optional[str] = None

    class Config:
        orm_mode = True  # Allow Pydantic to work with SQLAlchemy models

class ScreenerConfigCreate(ScreenerConfigBase):
    pass

class ScreenerConfigUpdate(ScreenerConfigBase):
    pass