from pydantic import BaseModel, Field
from typing import List, Optional, Literal

UNIVERSAL_CONFIG_SCHEMA_VERSION = 1

# Technicals
class SMAIndicator(BaseModel):
    period: int = Field(..., description="SMA period length, e.g. 30, 200, etc.")

class Technicals(BaseModel):
    sma_indicators: Optional[List[SMAIndicator]] = None
    candle_close_condition: Optional[Literal["green", "red", "any"]] = "any"
    candle_patterns: Optional[List[str]] = Field(
        None,
        description="List of desired candle patterns (e.g. 'doji', 'hammer', 'engulfing')"
    )

# Fundamentals
class Fundamentals(BaseModel):
    pe_ratio_min: Optional[float] = None
    pe_ratio_max: Optional[float] = None
    dividend_yield_min: Optional[float] = None
    dividend_yield_max: Optional[float] = None
    market_cap_min: Optional[float] = None
    market_cap_max: Optional[float] = None


# Volume
class Volume(BaseModel):
    min_avg_volume: Optional[int] = None
    max_avg_volume: Optional[int] = None


# General Filters
class General(BaseModel):
    symbols: Optional[List[str]] = None
    market: Optional[str] = None
    sector: Optional[str] = None
    industry: Optional[str] = None
    price_min: Optional[float] = None
    price_max: Optional[float] = None

# Universal Screener Config
class UniversalScreenerConfig(BaseModel):
    schema_version: int = Field(
        UNIVERSAL_CONFIG_SCHEMA_VERSION, description="Version of the universal config schema"
    )

    general: Optional[General] = None
    volume: Optional[Volume] = None
    fundamentals: Optional[Fundamentals] = None
    technicals: Optional[Technicals] = None

    extra_options: Optional[dict] = Field(
        default_factory=dict,
        description="Optional source-specific options"
    )