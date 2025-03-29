from pathlib import Path
from dataclasses import dataclass

# Project root (used for relative paths)
BASE_DIR = Path(__file__).resolve().parent.parent

# Individual DB config structure
@dataclass(frozen=True)
class SingleDatabase:
    name: str
    path: Path

# Full project DB config
@dataclass(frozen=True)
class DatabaseConfig:
    screener_results: SingleDatabase = SingleDatabase(
        name = "screener_results.db",
        path = BASE_DIR / "database" / "data" / "screener_results.db"
        )
    screener_configs: SingleDatabase = SingleDatabase(
        name = "screener_configs.db",
        path = BASE_DIR / "database" / "data" / "screener_configs.db"
        )
    
# Instantiate config
DB = DatabaseConfig()
    
# Define schema directory
SCHEMA_DIR = BASE_DIR / 'schema'