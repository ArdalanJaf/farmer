import pytest
from screener.schemas.universal_config import UniversalScreenerConfig, General, Fundamentals, Technicals, Volume
from screener.adapters.yahoo import map_to_yahoo


def test_map_to_yahoo_basic():
    config = UniversalScreenerConfig(
        schema_version=1,
        general=General(sector="Technology", price_min=10, price_max=200),
        fundamentals=Fundamentals(pe_ratio_min=5, pe_ratio_max=30),
        volume=Volume(min_avg_volume=1000000),
        technicals=Technicals(candle_close_condition="green")
    )

    query = map_to_yahoo(config)

    assert query["query"]["operator"] == "AND"
    criteria = query["query"]["criteria"]

    # Check sector filter
    sector_criteria = next((c for c in criteria if c["field"] == "sector"), None)
    assert sector_criteria is not None
    assert sector_criteria["operator"] == "eq"
    assert sector_criteria["value"] == "Technology"

    # Check price_min filter
    price_min = next((c for c in criteria if c["field"] == "price" and c["operator"] == "gt"), None)
    assert price_min["value"] == 10

    # Check price_max filter
    price_max = next((c for c in criteria if c["field"] == "price" and c["operator"] == "lt"), None)
    assert price_max["value"] == 200

    # Check PE ratio
    pe_min = next((c for c in criteria if c["field"] == "peRatio" and c["operator"] == "gt"), None)
    assert pe_min["value"] == 5

    pe_max = next((c for c in criteria if c["field"] == "peRatio" and c["operator"] == "lt"), None)
    assert pe_max["value"] == 30

    # Check volume
    volume_min = next((c for c in criteria if c["field"] == "averageVolume" and c["operator"] == "gt"), None)
    assert volume_min["value"] == 1000000

    # Check candle condition
    candle = next((c for c in criteria if c["field"] == "priceChangePercent"), None)
    assert candle is not None
    assert candle["operator"] == "gt"
    assert candle["value"] == 0
