import os
from src.extract.extract import extract_data
from src.load.load import load_data
from src.load.load import open_streamlit
from src.transform.transform import transform_data
from src.utils.logging_utils import setup_logger


def main():

    # Setup ETL pipeline logger
    logger = setup_logger("etl_pipeline", "etl_pipeline.log")

    try:

        logger.info("Starting ETL pipeline")

        # Extraction phase
        logger.info("Starting extraction phase")
        data = extract_data()

        # Transformation phase
        logger.info("Starting transformation phase")
        transformed_data = transform_data(data)

        # Load phase
        logger.info("Starting load phase")
        load_data(transformed_data)

        logger.info("Attempting to run streamlit")
        open_streamlit()

        print("ETL pipeline run successfully")
    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}")


if __name__ == "__main__":
    main()
