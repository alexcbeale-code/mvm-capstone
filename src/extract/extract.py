import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("extract_data", "extract_data.log")


def extract_data():
    logger.info("Extracting data to dataframe")
    df = pd.read_csv("data/raw/an_report_all_col_eval_1_2025-11-30-13-36.csv")
        
    return df
