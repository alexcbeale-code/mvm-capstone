import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("clean_final_report", "transform_data.log")


def clean_final_report(main: pd.DataFrame) -> pd.DataFrame:

    try:
        main.dropna(subset="email", inplace=True)
    except Exception as e:
        logger.error(f"Failed to execute dropping null values in email column: {e}")

    try:
        main.drop(["can2_lifetime_value"], axis=1, inplace=True)
    except Exception as e:
        logger.error(f"Failed to drop can2 columns: {e}")

    return main
