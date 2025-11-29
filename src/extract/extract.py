import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("extract_data", "extract_data.log")


def extract_data():
    logger.info("Extracting data to dataframe")
    df = pd.read_csv("data/raw/an_report_export_test_full_list_2_columns_2025-11-27-09-46.csv")
    return df
