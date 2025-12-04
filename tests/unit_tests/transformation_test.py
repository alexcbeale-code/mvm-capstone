from src.transform.tags import to_list_tags
from src.transform.clean_report import clean_final_report
from src.transform.normalise_column import normalise_columns
from src.transform.combine_donations import combine_donations
from src.transform.create_scores import create_scores
import pandas as pd

# fake uuids and fake tags generated with AI
# generated with non-sensitive examples


def test_transform_tags_to_list():

    df = pd.DataFrame({
            "user_tags": ["VIP / Platinum member, Admin / Super user / Finance / Refund access",
                          "User / Trial period, Marketing / Promo code used, Exclude / Inactive user",
                          "VIP / Gold member"]
        })

    result = to_list_tags(df)

    assert len(result) == len(df)  # nothing should have been lost or gained
    assert len(result.iloc[0]["user_tags"]) == 2  # this tag should only have been split twice
    assert type(result.iloc[0]["user_tags"]) is list  # needs to be list of string not string


def test_clean_report_function():

    df = pd.DataFrame({
        "email": ["iamanemail@yoohoo.com", "literallyGod@heaven.gov", None, "hiEDhowsMyTesting?"],
        "lifetime_value": [-5000, 9999999, 1.333333333333333, 10],
        "user_tags": ["VIP / Platinum member, Admin / Super user, Finance / Refund access", None, "i am a tag yay ^-^", None],
        "uuid": ["5a1d9c3b-7e8f-42a6-8c2d-1b0e5f4a9c7b", "steve", None, None]  # NOT REAL IDS
    })

    original_row_count = len(df)

    result = clean_final_report(df.copy())

    assert len(result) == original_row_count - 1  # 1 email should have been removed
    assert result["email"].isnull().sum() == 0  # there should be no nulls
    assert result["user_tags"].isnull().sum() == 0  # there should be no nulls
    assert "lifetime_value" not in result.columns  # this should have been dropped
    assert ["email", "user_tags", "uuid"] == list(result.columns)  # only columns which should exist still
    assert (result["user_tags"].loc[result["user_tags"] == "no_tags"]).any()


def test_normalise_column():

    df = pd.DataFrame({
        "Email": ["iamanemail@yoohoo.com", "literallyGod@heaven.gov", None, "hiEDhowsMyTesting?"],
        "can2_Lifetime Value": [-5000, 9999999, 1.333333333333333, 10],
        "can2_User Tags": ["VIP / Platinum member, Admin / Super user, Finance / Refund access", None, "i am a tag yay ^-^", None],
        "uuid": ["5a1d9c3b-7e8f-42a6-8c2d-1b0e5f4a9c7b", "steve", None, None]  # NOT REAL IDS
    })

    result = normalise_columns([df, df, df])

    assert len(result) == 3  # should return same dfs as put in 
    assert result[0].columns[0] == "email"  # should have lowered everything
    assert result[0].columns[2] == "user_tags"  # should remove can2 and replace space with _
    assert result[2].columns[1] == "lifetime_value"
    assert len(result[1]) == 4


def test_combine_donations():

    main = pd.DataFrame({
        "email": ["iamanemail@woohoo.com", "literallyGod@heaven.gov", None, "hiEDhowsMyTesting?"],
        "lifetime_value": [-5000, 9999999, 1.333333333333333, 10],
        "user_tags": ["VIP / Platinum member, Admin / Super user, Finance / Refund access", None, "i am a tag yay ^-^", None],
        "uuid": ["5a1d9c3b-7e8f-42a6-8c2d-1b0e5f4a9c7b", "steve", None, None]  # NOT REAL IDS
    })

    donations = pd.DataFrame({
        "email": ["iamanemail@woohoo.com",
                  "literallyGod@heaven.gov",
                  None,
                  "hiEDhowsMyTesting?",
                  "literallyGod@heaven.gov",
                  "iamanemail@woohoo.com"],
        "donation_amount": [12, 45, 2, 15, 22, 9]})

    result = combine_donations(main, donations)

    original_row_count = len(main)

    assert original_row_count == len(result)  # nothing should have changed

    # 12 + 9, this should have been summed
    assert result.loc[result["email"] == "iamanemail@woohoo.com", "donation_amount"].item() == 21
    # 45 + 22, this should have been summed
    assert result.loc[result["email"] == "literallyGod@heaven.gov", "donation_amount"].item() == 67
    assert result["donation_amount"].sum() == 103.0  # total of all donations, summation of sums
    assert len(result.columns) == 6 # only 2 cols added


def test_create_scores():

    main = pd.DataFrame({
        "email": ["iamanemail@woohoo.com", "literallyGod@heaven.gov", None, "hiEDhowsMyTesting?"],
        "lifetime_value": [-5000, 9999999, 1.333333333333333, 10],
        "user_tags": ["VIP / Platinum member, Admin / Super user, Finance / Refund access", None, "i am a tag yay ^-^", None],
        "uuid": ["5a1d9c3b-7e8f-42a6-8c2d-1b0e5f4a9c7b", "steve", None, None],  # NOT REAL IDS
        "donation_amount": [44, 25, 711, 0],
        "donation_count": [1, 2, 5, 0],
        "actions_taken": [5, 2, 0, 22]
    })

    result = create_scores(main)

    assert len(result.columns) == 11  # 4 cols added
    assert result["engagement_score"].isnull().sum() == 0  # nulls in engagement should be made 0
    assert (result["actions_taken_score"] == 0).any() == False  # all 0s should be null
    assert result["engagement_score"].iloc[0] == 0.75
