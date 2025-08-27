import pandas as pd
import logging


logger = logging.getLogger(__name__)

def extract(path="data/sales.csv"):
    try:
        df = pd.read_csv(path)
        logger.info(f"Loaded data from {path} with shape {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise