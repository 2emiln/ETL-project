import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform(df):
    try:
        result = df.groupby("city")["total"].sum().reset_index()
        result = result.rename(columns={"total": "total_sales"})
        logger.info("Data transformerad: summering per stad")
        return result
    except Exception as e:
        logger.error(f"Fel vid transformering: {e}")
        raise