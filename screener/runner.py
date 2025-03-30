from sqlalchemy.orm import Session
from database.models.screener_configs import ScreenerConfig as ScreenerConfigModel
from database.models.screener_results import ScreenerResult
from screener.schemas.universal_config import UniversalScreenerConfig
from screener.adapters.yahoo import map_to_yahoo
from database.crud import get_screener_config
from common.enums.screener_source import ScreenerSource

# Adapter map for multi-source support
ADAPTER_MAP = {
    ScreenerSource.YAHOO: map_to_yahoo,
    # ScreenerSource.IBKR: map_to_ibkr (future)
}

def run_screener(db: Session, config_id: int, source: ScreenerSource):
    # 1. Load config
    db_config: ScreenerConfigModel = get_screener_config(db, config_id)
    if not db_config:
        raise ValueError(f"ScreenerConfig with id {config_id} not found")

    # 2. Validate & parse config JSON
    try:
        validated_config = UniversalScreenerConfig(**db_config.config_json)
    except Exception as e:
        raise ValueError(f"Invalid config JSON: {e}")

    # 3. Map to source query
    adapter = ADAPTER_MAP.get(source)
    if not adapter:
        raise NotImplementedError(f"Source '{source}' not supported yet")
    
    query = adapter(validated_config)

    # 4. Fetch market data (stub for now)
    print(f"Running {source} Screener with query:\n{query}")
    fake_results = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]  # Replace later with real data fetch

    # 5. Save screener result
    db_result = ScreenerResult(
        config_id=db_config.id,
        config_snapshot=db_config.config_json,
        results_json=fake_results,
        source=source,
        api_version=None  # Add API version if you want
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)

    # 6. Print summary
    print(f"Screener run completed. {len(fake_results)} results saved.")
    return db_result
