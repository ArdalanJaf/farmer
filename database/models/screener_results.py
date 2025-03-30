from enum import StrEnum
from sqlalchemy import Column, Integer, DateTime, JSON, ForeignKey, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database.db import Base
from screener.schemas.source_enums import ScreenerSource

class ScreenerResult(Base):
    __tablename__ = "screener_results"

    id = Column(Integer, primary_key=True, index=True)
    config_id = Column(Integer, ForeignKey("screener_configs.id"), nullable=False)
    config_snapshot = Column(JSON, nullable=False)
    results_json = Column(JSON, nullable=False)
    source = Column(StrEnum(ScreenerSource), nullable=False) 
    api_version = Column(String, nullable=True)  # Optional
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship to ScreenerConfig
    config = relationship("ScreenerConfig", back_populates="results")
