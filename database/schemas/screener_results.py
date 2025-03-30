from pydantic import BaseModel
from typing import Dict

# ScreenerResult CRUD-ops DTOs
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

