import pandas as pd
from src.utils.logging_utils import setup_logger
from extract_actions import combine_action_data_with_main

logger = setup_logger("extract_data", "extract_data.log")


def extract_data():
    '''
    Get the action data into the main report 
    Extract the donation data  
    '''
    logger.info("Extracting data to dataframe")
    
    df = pd.read_csv("data/raw/main_report.csv")
    
    
    return df
