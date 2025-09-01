import logging
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)

def load_to_sql(df, db_url="sqlite:///data/processed/sales_per_city.db", table_name="sales_per_city"):
    try:
        engine = create_engine(db_url)
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        logger.info(f"Loaded {len(df)} rows to {table_name} @ {db_url}")
    except Exception as e:
        logger.error(f"Error on loading data: {e}")
        raise
