import pandas as pd
import logging


logger = logging.getLogger(__name__)

def extract(path="data/raw/sales.csv"):
    try:
        df = pd.read_csv(path)
        logger.info(f"Loaded data from {path}.")
        return df
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise