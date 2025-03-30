from pydantic import BaseModel
from typing import Optional, Dict

# Define the schema for ScreenerConfig
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

# Define the schema for ScreenerResult
class ScreenerResultBase(BaseModel):
    config_id: int
    config_snapshot: Dict
    results_json: Dict

    class Config:
        orm_mode = True

class ScreenerResultCreate(ScreenerResultBase):
    pass

class ScreenerResultUpdate(ScreenerResultBase):
    pass
