from src.utils.logging_utils import setup_logger
from src.extract.extract_actions import combine_action_data_with_main
from src.extract.extract_donations import extract_donations
from src.extract.extract_main import extract_main

logger = setup_logger("extract_data", "extract_data.log")


def extract_data() -> list:
    '''
    Get the action data into the main report
    Extract the donation data
    '''
    logger.info("Extracting main report to dataframe")

    try:
        df = extract_main()
    except Exception as e:
        logger.error(f"Fatal error: Failed to extract main report data: {e}")
        return
    logger.info("Joining action data to main report")

    try:
        df = combine_action_data_with_main(df)
    except Exception as e:
        logger.error(f"Fatal error: Failed to combine action data: {e}")
        return

    logger.info("Extracting donation data")

    try:
        dono_df = extract_donations()
    except Exception as e:
        logger.error(f"Fatal error: Failed to extract donation data: {e}")
        return
    return [df, dono_df]
