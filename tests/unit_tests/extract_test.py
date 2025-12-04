import pandas as pd
from src.extract.extract_donations import extract_donations
from src.extract.extract_main import extract_main


def test_donation_extraction():

    result = extract_donations()

    assert isinstance(result, pd.DataFrame)
    assert (result["Donation Amount"] >= 0).all()

    columns_which_should_exist = ["Email", "Donation Amount"]
    assert all(col in result.columns for col in columns_which_should_exist)


def test_main_extraction():

    result = extract_main()

    assert isinstance(result, pd.DataFrame)
    assert (result["can2_lifetime_value"] >= 0).all()

    columns_which_should_exist = ["email", "can2_user_tags"]

    # must have AT LEAST columns in above list
    for col in columns_which_should_exist:
        assert col in result.columns
