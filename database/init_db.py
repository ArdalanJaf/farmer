import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from database.db import screener_configs_engine, screener_results_engine, Base
from database.models.screener_configs import ScreenerConfig
from database.models.screener_results import ScreenerResult

def init_db():
    try:
        # List of (engine, table object, label) for each DB
        db_tables = [
            (screener_configs_engine, ScreenerConfig.__table__, "screener_configs"),
            (screener_results_engine, ScreenerResult.__table__, "screener_results"),
        ]

        # Create each DB table
        for engine, table, label in db_tables:
            print(f"Creating {label} DB...")
            Base.metadata.create_all(bind=engine, tables=[table])

        print("✅ Databases initialized.")

    except Exception as e:
        # Log any errors during table creation
        print(f"❌ Error initializing databases: {e}")

if __name__ == "__main__":
    # Run init when script is called directly
    init_db()
