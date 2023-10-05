import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# ==============================================================================================


def get_rs_data(file_name="Restaurant_Scores_-_LIVES_Standard 1.csv") -> pd.DataFrame:
    '''This function takes in the file name provided. 
        It will pull the file to your notebook.
        '''
    return pd.read_csv(file_name)

# ==============================================================================================


def prep_rs_data(df: pd.DataFrame) -> pd.DataFrame:
    '''this file takes in a pandas df
        Will drop the following columns
        Then drop all null values
        converts inspection_date to datetime variable
        sets inspection_date as index
        creates 2 new columns year and month
    '''
    df = df.drop(
        [
            "Analysis Neighborhoods",
            "Current Supervisor Districts",
            "Current Police Districts",
            "SF Find Neighborhoods",
            "Neighborhoods",
            "business_phone_number",
            "business_id",
            "business_city",
            "business_state",
        ],
        axis=1,
    )
    df = df.dropna()
    df.inspection_date = pd.to_datetime(df.inspection_date)
    df = df.set_index("inspection_date").sort_index()
    df["Year"] = df.index.year  # created columns using the index
    df["Month"] = df.index.month
    return df


# ==============================================================================================


def categorize_business(business_name):
    # Convert the business name to lowercase for case-insensitive matching
    lower_case_name = business_name.lower()
    '''Uses key words to lable data the business column
        '''

    if (
        "cafe" in lower_case_name
        or "bakery" in lower_case_name
        or "coffee" in lower_case_name
        or "starbucks" in lower_case_name
        or 'creamery' in lower_case_name
        or 'pastry' in lower_case_name
        or 'donut' in lower_case_name
        or 'donuts' in lower_case_name
        or 'cakes' in lower_case_name
    ):
        return "Cafe & Bakery"
    if (
        "deli " in lower_case_name
        or "delight" in lower_case_name
        or "restaurant" in lower_case_name
        or "house" in lower_case_name
        or "bbq" in lower_case_name
        or "kitchen" in lower_case_name
        or "taqueria" in lower_case_name
        or "food" in lower_case_name
        or "foods" in lower_case_name
        or "taste" in lower_case_name
        or "wild" in lower_case_name
        or "restaurante" in lower_case_name
        or "borrito" in lower_case_name
        or "eats" in lower_case_name
        or "fish" in lower_case_name
        or "subway" in lower_case_name
        or "little" in lower_case_name
        or "company" in lower_case_name
    ):
        return "Restaurant"
    if "school" in lower_case_name or "university" in lower_case_name:
        return "Education"
    if "club" in lower_case_name:
        return "Club"
    if "pizza" in lower_case_name:
        return "Pizza Shop"
    if "liquor" in lower_case_name or "safeway" in lower_case_name:
        return "Store"
    else:
        return "Other"

# ==============================================================================================

def split_data(
    df: pd.DataFrame,
    category: str,
    train_size: float = 0.7,
    val_size: float = 0.15,
    test_size: float = 0.15,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    df = df[df.business_category == category]
    df_score = df[["inspection_score"]]

    n = df_score.shape[0]
    train_end_index = round(train_size * n)
    val_end_index = train_end_index + round(val_size * n)

    train = df_score[:train_end_index]
    val = df_score[train_end_index:val_end_index]
    test = df_score[val_end_index:]
    return (train, val, test)

# ==============================================================================================

def plot_train_data(train: pd.DataFrame, val: pd.DataFrame, test: pd.DataFrame) -> None:
    plt.plot(train.index, train.inspection_score)
    plt.plot(val.index, val.inspection_score)
    plt.plot(test.index, test.inspection_score)
# ==============================================================================================

# if __name__ == '__main__'