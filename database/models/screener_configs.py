from sqlalchemy import Column, Integer, DateTime, JSON, ForeignKey, String, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database.db import Base

class ScreenerConfig(Base):
    __tablename__ = "screener_configs"
    __table_args__ = (UniqueConstraint("name", "version", name="uq_name_version"))

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    version = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    config_json = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    results = relationship("ScreenerResult", back_populates="config")
