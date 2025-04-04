from database.crud.screener_configs import create_screener_config, update_screener_config
from database.schemas.screener_configs import ScreenerConfigCreate, ScreenerConfigUpdate
from screener.schemas.universal_config import UniversalScreenerConfig

def test_create_screener_config_success(test_session):
    config = UniversalScreenerConfig(schema_version=1)
    dto = ScreenerConfigCreate(
        name="Test Strategy",
        version=1,
        description="Test description",
        config_json=config.model_dump()
    )

    created = create_screener_config(test_session, dto)
    assert created.id is not None
    assert created.name == "Test Strategy"
    assert created.version == 1

def test_update_screener_config_success(test_session):
    # Create first
    config = UniversalScreenerConfig(schema_version=1)
    dto = ScreenerConfigCreate(
        name="Original",
        version=1,
        description="Before update",
        config_json=config.model_dump()
    )
    created = create_screener_config(test_session, dto)

    # Update
    updated_dto = ScreenerConfigUpdate(
        name="Updated",
        version=2,
        description="After update",
        config_json=config.model_dump()
    )
    updated = update_screener_config(test_session, created.id, updated_dto)

    assert updated.name == "Updated"
    assert updated.version == 2
    assert updated.description == "After update"

def test_update_screener_config_not_found(test_session):
    config = UniversalScreenerConfig(schema_version=1)
    dto = ScreenerConfigUpdate(
        name="Missing",
        version=1,
        description="Not real",
        config_json=config.model_dump()
    )
    result = update_screener_config(test_session, screener_config_id=999, dto=dto)
    assert result is None
