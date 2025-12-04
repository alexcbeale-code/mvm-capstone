import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("extract_main", "extract_data.log")


def extract_main():

    df = pd.read_csv("data/raw/main_report.csv")
    return df
