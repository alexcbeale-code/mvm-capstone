import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("combine_donations", "transform_data.log")


def combine_donations(main: pd.DataFrame, donations: pd.DataFrame) -> pd.DataFrame:
    '''
    Group donations by email
    Create donation count column
    Set email as index
    Join to main
    '''
    try:
        columns_to_group = ["email", "donation_amount"]
        grouped_donations = donations[columns_to_group].groupby("email").sum()
        count_of_each_email = donations.groupby("email").size()
    except Exception as e:
        logger.error(f"Failed to aggregate donation data and create count column: {e}")
        return main

    try:
        donation_df_to_join_main = grouped_donations.merge(count_of_each_email.rename("donation_count"), how="left", on="email")

        combined_report = main.merge(donation_df_to_join_main, how="left", on="email")
    except Exception as e:
        logger.error(f"Failed to join donation data to main: {e}")
        return main

    return combined_report
