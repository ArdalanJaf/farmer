from screener.schemas.universal_config import UniversalScreenerConfig
from typing import Dict, Any, List


def map_to_yahoo(config: UniversalScreenerConfig) -> Dict[str, Any]:
    """
    Maps UniversalScreenerConfig to Yahoo Screener query format.
    """
    criteria: List[Dict[str, Any]] = []

    # General filters
    if config.general:
        if config.general.sector:
            criteria.append({
                "field": "sector",
                "operator": "eq",
                "value": config.general.sector
            })
        if config.general.industry:
            criteria.append({
                "field": "industry",
                "operator": "eq",
                "value": config.general.industry
            })
        if config.general.price_min is not None:
            criteria.append({
                "field": "price",
                "operator": "gt",
                "value": config.general.price_min
            })
        if config.general.price_max is not None:
            criteria.append({
                "field": "price",
                "operator": "lt",
                "value": config.general.price_max
            })

    # Volume
    if config.volume:
        if config.volume.min_avg_volume is not None:
            criteria.append({
                "field": "averageVolume",
                "operator": "gt",
                "value": config.volume.min_avg_volume
            })
        if config.volume.max_avg_volume is not None:
            criteria.append({
                "field": "averageVolume",
                "operator": "lt",
                "value": config.volume.max_avg_volume
            })

    # Fundamentals
    if config.fundamentals:
        if config.fundamentals.pe_ratio_min is not None:
            criteria.append({
                "field": "peRatio",
                "operator": "gt",
                "value": config.fundamentals.pe_ratio_min
            })
        if config.fundamentals.pe_ratio_max is not None:
            criteria.append({
                "field": "peRatio",
                "operator": "lt",
                "value": config.fundamentals.pe_ratio_max
            })
        if config.fundamentals.market_cap_min is not None:
            criteria.append({
                "field": "marketCap",
                "operator": "gt",
                "value": config.fundamentals.market_cap_min
            })
        if config.fundamentals.market_cap_max is not None:
            criteria.append({
                "field": "marketCap",
                "operator": "lt",
                "value": config.fundamentals.market_cap_max
            })

    # Techncials - Candle close condition
    if config.technicals and config.technicals.candle_close_condition:
        if config.technicals.candle_close_condition == "green":
            criteria.append({
                "field": "priceChangePercent",
                "operator": "gt",
                "value": 0
            })
        elif config.technicals.candle_close_condition == "red":
            criteria.append({
                "field": "priceChangePercent",
                "operator": "lt",
                "value": 0
            })

    # Extra options
    if config.extra_options:
        # Optionally merge any direct Yahoo-specific filters here
        for key, value in config.extra_options.items():
            criteria.append({
                "field": key,
                "operator": "eq",
                "value": value
            })

    # Assemble full query payload
    query = {
        "offset": 0,
        # TODO: this will need to be configurable at time of executing screener
        "size": 100,
        "sortField": "marketCap",
        "sortType": "DESC",
        "quoteType": "EQUITY",
        "query": {
            "operator": "AND",
            "criteria": criteria
        }
    }

    return query