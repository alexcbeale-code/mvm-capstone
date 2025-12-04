import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("normalise_columns", "transform_data.log")


def normalise_columns(dataframes: list) -> list:

    normalised_columns = []

    for df in dataframes:
        try:
            df.columns = df.columns.str.lower().str.replace(" ", "_")
            df.columns = df.columns.str.replace("can2_", "")
            normalised_columns.append(df)
        except Exception as e:
            logger.error(f"Failed to noramlise column names for {df}: {e}")

    return dataframes
