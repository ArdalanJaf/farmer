import pytest
from screener.runner import run_screener
from screener.enums import ScreenerSource
from screener.schemas.universal_config import UniversalScreenerConfig
from database.models.screener_configs import ScreenerConfig as ScreenerConfigModel
from database.models.screener_results import ScreenerResult

def test_run_screener_success(test_session):
    """Test running the screener with valid configuration and source."""
    # Arrange: Create and insert a mock screener configuration
    mock_config = UniversalScreenerConfig(schema_version=1)
    db_config = ScreenerConfigModel(
        name="Test Config",
        version=1,
        description="A test configuration",
        config_json=mock_config.model_dump()
    )
    test_session.add(db_config)
    test_session.commit()

    # Act: Execute the screener function
    result = run_screener(test_session, db_config.id, ScreenerSource.YAHOO)

    # Assert: Validate the results
    assert result is not None
    assert result.config_id == db_config.id
    assert len(result.results_json) == 2  # Assuming the fake results contain 2 entries
    assert result.results_json[0]["symbol"] == "AAPL"
    assert result.results_json[1]["symbol"] == "MSFT"

    # Clean up: Remove the inserted data
    test_session.delete(result)
    test_session.delete(db_config)
    test_session.commit()
