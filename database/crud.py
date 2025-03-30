from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from database.models.screener_configs import ScreenerConfig
from database.models.screener_results import ScreenerResult
from database.schemas import ScreenerConfigCreate, ScreenerConfigUpdate, ScreenerResultCreate, ScreenerResultUpdate  # <-- Using schemas

# -----------------------------
# CRUD for ScreenerConfig Model
# -----------------------------

# Create a new ScreenerConfig
def create_screener_config(
    db: Session,
    dto: ScreenerConfigCreate  # <-- Using schema for input validation
) -> ScreenerConfig:
    db_screener_config = ScreenerConfig(
        name=dto.name,
        version=dto.version,
        config_json=dto.config_json,
        description=dto.description,
    )
    db.add(db_screener_config)
    db.commit()
    db.refresh(db_screener_config)
    return db_screener_config

# Update a ScreenerConfig
def update_screener_config(
    db: Session,
    screener_config_id: int,
    dto: ScreenerConfigUpdate 
) -> Optional[ScreenerConfig]:
    db_screener_config = db.query(ScreenerConfig).filter(ScreenerConfig.id == screener_config_id).first()
    if db_screener_config:
        db_screener_config.name = dto.name
        db_screener_config.version = dto.version
        db_screener_config.config_json = dto.config_json
        db_screener_config.description = dto.description
        db.commit()
        db.refresh(db_screener_config)
        return db_screener_config
    return None

# Get a ScreenerConfig by ID
def get_screener_config_by_id(db: Session, screener_config_id: int) -> Optional[ScreenerConfig]:
    return db.query(ScreenerConfig).filter(ScreenerConfig.id == screener_config_id).first()

# Get all ScreenerConfigs with pagination
def get_all_screener_configs(db: Session, skip: int = 0, limit: int = 100) -> List[ScreenerConfig]:
    return db.query(ScreenerConfig).offset(skip).limit(limit).all()

# Delete a ScreenerConfig
def delete_screener_config(db: Session, screener_config_id: int) -> Optional[ScreenerConfig]:
    db_screener_config = db.query(ScreenerConfig).filter(ScreenerConfig.id == screener_config_id).first()
    if db_screener_config:
        db.delete(db_screener_config)
        db.commit()
        return db_screener_config
    return None

# -----------------------------
# CRUD for ScreenerResult Model
# -----------------------------

# Create a new ScreenerResult
def create_screener_result(
    db: Session,
    dto: ScreenerResultCreate 
) -> ScreenerResult:
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
    if db_screener_result:
        db_screener_result.config_id = dto.config_id
        db_screener_result.config_snapshot = dto.config_snapshot
        db_screener_result.results_json = dto.results_json
        db.commit()
        db.refresh(db_screener_result)
        return db_screener_result
    return None

# Get a ScreenerResult by ID
def get_screener_result_by_id(db: Session, screener_result_id: int) -> Optional[ScreenerResult]:
    return db.query(ScreenerResult).filter(ScreenerResult.id == screener_result_id).first()

# Get all ScreenerResults for a specific ScreenerConfig
def get_screener_results_for_config(db: Session, config_id: int) -> List[ScreenerResult]:
    return db.query(ScreenerResult).filter(ScreenerResult.config_id == config_id).all()

# Delete a ScreenerResult
def delete_screener_result(db: Session, screener_result_id: int) -> Optional[ScreenerResult]:
    db_screener_result = db.query(ScreenerResult).filter(ScreenerResult.id == screener_result_id).first()
    if db_screener_result:
        db.delete(db_screener_result)
        db.commit()
        return db_screener_result
    return None
