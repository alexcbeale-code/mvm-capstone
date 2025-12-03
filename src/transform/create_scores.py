import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("create_scores", "transform_data.log")


def create_scores(combined_report: pd.DataFrame) -> pd.DataFrame:

    try:
        combined_report["donation_size_score"] = (combined_report["donation_amount"].rank(pct=True))
    except Exception as e:
        logger.error(f"Failed to create donation size scores: {e}")

    try:
        combined_report["donation_freq_score"] = (combined_report["donation_count"].rank(pct=True))
    except Exception as e:
        logger.error(f"Failed to create donation frequency scores: {e}")

    try:
        combined_report["actions_taken_score"] = (combined_report["actions_taken"].rank(pct=True))
    except Exception as e:
        logger.error(f"Failed to create actions taken score: {e}")

    try:
        combined_report["engagement_score"] = ((combined_report["donation_size_score"].fillna(0)
                                                + combined_report["actions_taken_score"].fillna(0)) / 2)
    except Exception as e:
        logger.error(f"Failed to create engagement score: {e}")

    return combined_report
