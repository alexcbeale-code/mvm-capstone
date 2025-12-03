import pandas as pd
from src.utils.logging_utils import setup_logger


logger = setup_logger("extract_donations", "extract_data.log")


def extract_donations() -> pd.DataFrame:

    df = pd.read_csv("data/raw/donations.csv")

    return df
