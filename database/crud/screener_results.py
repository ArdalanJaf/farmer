from sqlalchemy.orm import Session
from typing import List, Optional
from database.models.screener_results import ScreenerResult
from database.schemas.screener_results import ScreenerResultCreate, ScreenerResultUpdate
from database.utils import validate_json

# -----------------------------
# CRUD for ScreenerResult Model
# -----------------------------

# Create a new ScreenerResult
def create_screener_result(
    db: Session,
    dto: ScreenerResultCreate 
) -> ScreenerResult:
    # TODO: validate json

    db_screener_result = ScreenerResult(
        config_id=dto.config_id,
        config_snapshot=dto.config_snapshot,
        results_json=dto.results_json,
    )
    db.add(db_screener_result)
    db.commit()
    db.refresh(db_screener_result)
    return db_screener_result

# Update a ScreenerResult
def update_screener_result(
    db: Session,
    screener_result_id: int,
    dto: ScreenerResultUpdate 
) -> Optional[ScreenerResult]:
    db_screener_result = db.query(ScreenerResult).filter(ScreenerResult.id == screener_result_id).first()

    if not db_screener_result:
       raise ValueError(f"ScreenerResult with id {screener_result_id} not found")
    
    # TODO: validate json

    db_screener_result.config_id = dto.config_id
    db_screener_result.config_snapshot = dto.config_snapshot
    db_screener_result.results_json = dto.results_json
    db.commit()
    db.refresh(db_screener_result)
    return db_screener_result
    

# Get a ScreenerResult by ID
def get_screener_result_by_id(db: Session, screener_result_id: int) -> Optional[ScreenerResult]:
    return db.query(ScreenerResult).filter(ScreenerResult.id == screener_result_id).first()

# Get all ScreenerResults for a specific ScreenerConfig
def get_screener_results_for_config(db: Session, config_id: int) -> List[ScreenerResult]:
    return db.query(ScreenerResult).filter(ScreenerResult.config_id == config_id).all()

# Delete a ScreenerResult
def delete_screener_result(db: Session, screener_result_id: int) -> Optional[ScreenerResult]:
    db_screener_result = db.query(ScreenerResult).filter(ScreenerResult.id == screener_result_id).first()
    if not db_screener_result:
        return False
    
    db.delete(db_screener_result)
    db.commit()
    return True
