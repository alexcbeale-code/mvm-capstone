import pandas as pd
from src.utils.logging_utils import setup_logger

logger = setup_logger("tags", "transform_data.log")


def to_list_tags(main: pd.DataFrame) -> pd.DataFrame:

    try:
        main["user_tags"] = pd.DataFrame(main["user_tags"].str.split(","))
    except Exception as e:
        logger.error(f"Failed to put tags into a list: {e}")
    return main


def create_supports_reform_col(main: pd.DataFrame) -> pd.DataFrame:

    reform_tags = ["Oct2025_support-farage",
                   "Possibly_Reform",
                   "Confirmed_Reform",
                   "Aug-2025_vote_reform"
                   ]
    try:
        main["supports_reform"] = main["user_tags"].map(
            lambda user_tags: isinstance(user_tags, list)
            and any(tag in reform_tags for tag in user_tags))
    except Exception as e:
        logger.error(f"Failed to create supports_reform column: {e}")
    return main


def create_against_reform_col(main: pd.DataFrame) -> pd.DataFrame:

    reform_tags = ["Oct2025_anti-farage"]
    try:
        main["against_reform"] = main["user_tags"].map(
            lambda user_tags: isinstance(user_tags, list)
            and any(tag in reform_tags for tag in user_tags))
    except Exception as e:
        logger.error(f"Failed to create supports_reform column: {e}")
    return main


def create_party_cols(main: pd.DataFrame) -> pd.DataFrame:

    party_tags = ["Aug-2025_vote_your",
                  "Aug-2025_vote_libdem",
                  "Aug-2025_vote_labour",
                  "Aug-2025_vote_conservative",
                  "Aug-2025_vote_green",
                  ]

    for tag in party_tags:
        try:
            col_name = tag.split("_")[2]
            main[f"supports_{col_name}"] = main["user_tags"].map(
                lambda user_tags: isinstance(user_tags, list)
                and tag in user_tags)
        except Exception as e:
            logger.error(f"Failed to create party column column: {e}")
    return main
