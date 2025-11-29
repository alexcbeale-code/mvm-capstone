import pandas as pd
from src.utils.logging_utils import setup_logger


logger = setup_logger("transform_data", "transform_data.log")


def transform_data(raw_data):
    logger.info("Tranforming data")
    clean_data = raw_data.dropna()
    return clean_data
