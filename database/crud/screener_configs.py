from sqlalchemy.orm import Session
from typing import List, Optional
from database.models.screener_configs import ScreenerConfig
from database.schemas.screener_configs import ScreenerConfigCreate, ScreenerConfigUpdate
from database.utils import validate_json
from screener.schemas.universal_config import UniversalScreenerConfig 

# -----------------------------
# CRUD for ScreenerConfig Model
# -----------------------------

# Create a new ScreenerConfig
def create_screener_config(
    db: Session,
    dto: ScreenerConfigCreate
) -> ScreenerConfig:
    clean_config = validate_json(dto.config_json, UniversalScreenerConfig)

    db_screener_config = ScreenerConfig(
        name=dto.name,
        version=dto.version,
        config_json=clean_config,
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

    if not db_screener_config:
        return None
    
    clean_config = validate_json(dto.config_json, UniversalScreenerConfig)
    
    db_screener_config.name = dto.name
    db_screener_config.version = dto.version
    db_screener_config.config_json = clean_config
    db_screener_config.description = dto.description
    db.commit()
    db.refresh(db_screener_config)
    return db_screener_config

# Get a ScreenerConfig by ID
def get_screener_config_by_id(db: Session, screener_config_id: int) -> Optional[ScreenerConfig]:
    return db.query(ScreenerConfig).filter(ScreenerConfig.id == screener_config_id).first()

# Get all ScreenerConfigs with pagination
def get_all_screener_configs(db: Session, skip: int = 0, limit: int = 100) -> List[ScreenerConfig]:
    return db.query(ScreenerConfig).offset(skip).limit(limit).all()

# Delete a ScreenerConfig
def delete_screener_config(db: Session, screener_config_id: int) -> Optional[ScreenerConfig]:
    db_screener_config = db.query(ScreenerConfig).filter(ScreenerConfig.id == screener_config_id).first()
    if not db_screener_config:
        return False

    db.delete(db_screener_config)
    db.commit()
    return True