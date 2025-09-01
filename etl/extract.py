import pandas as pd
import logging


logger = logging.getLogger(__name__)

def extract(path="data/raw/sales.csv"):
    try:
        df = pd.read_csv(path)
        logger.info(f"Loaded data from {path} with shape {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Error vid inhämtning av data: {e}")
        raise