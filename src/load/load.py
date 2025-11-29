from src.utils.logging_utils import setup_logger
import pandas as pd
import os

logger = setup_logger("load_data", "load_data.log")


def load_data(data):
    save_dir = "data/processed/ready_data.feather"
    logger.info("Loading data into feather")
    try:
        data.to_feather(save_dir)
        logger.info(f"Successfully loaded dataframe to feather at {save_dir}")
    except Exception as e:
        logger.error(f"Failed to save dataframe to feather at {save_dir} : {e}")


def open_streamlit():

    command = "streamlit run src/load/app.py"
    os.system(command)
