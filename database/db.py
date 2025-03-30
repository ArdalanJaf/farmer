from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.settings import db

# DB URLs
SCREENER_CONFIGS_URL = f"sqlite:///{db.screener_configs.path}"
SCREENER_RESULTS_URL = f"sqlite:///{db.screener_results.path}"

# Engines
screener_configs_engine = create_engine(SCREENER_CONFIGS_URL, connect_args={"check_same_thread": False})
screener_results_engine = create_engine(SCREENER_RESULTS_URL, connect_args={"check_same_thread": False})

# Sessions
ScreenerConfigsSession = sessionmaker(autocommit=False, autoflush=False, bind=screener_configs_engine)
ScreenerResultsSession = sessionmaker(autocommit=False, autoflush=False, bind=screener_results_engine)

# Base
Base = declarative_base()
