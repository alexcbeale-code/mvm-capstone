import pandas as pd
from src.utils.logging_utils import setup_logger
from src.transform.combine_donations import combine_donations
from src.transform.create_scores import create_scores
from src.transform.normalise_column import normalise_columns
from src.transform.clean_report import clean_final_report

logger = setup_logger("transform_data", "transform_data.log")


def transform_data(main: pd.DataFrame, donations: pd.DataFrame) -> pd.DataFrame:
    '''
    Normalise columns
    Action score
    donation size and freq score
    donation count and total value on main
    total engagement score
    '''
    logger.info("Attempting to normalise columns")
    # applies .lower and .strip to all column names
    main, donations = normalise_columns([main, donations])

    logger.info("Attempting to combine donation data with main")
    # Groups all donations by email and uses .size() to create donation count column
    # and joins them all to main. Non-donors have NaN in both columns which is correct
    # adds donation_amount (sum of all donations), donation_count (count of donations) columns to main
    combined_report = combine_donations(main, donations)

    logger.info("Attempting to generate engagement scores")
    # Creates 4 new columns in main report: donation_size_score, donation_freq_score,
    # actions_taken_score and engagement_score
    # The first 3 are rank(pct=True) ie distribution scores
    # Engagement score treats NaN values as 0
    # Engagement score is 50/50 for actions and donations ie they are equal weight
    combined_scored_report = create_scores(combined_report)

    logger.info("Attempting to clean final report")
    # Drops any 'can2' columns
    # Removes any records with null emails
    clean_combined_scored_report = clean_final_report(combined_scored_report)

    return clean_combined_scored_report
