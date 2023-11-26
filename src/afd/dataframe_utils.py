# dataframe_utils.py

import pandas as pd

def row_count(df):
    """
    Returns the number of rows in the DataFrame.

    :param df: Pandas DataFrame.
    :return: Number of rows.
    """
    if isinstance(df, pd.DataFrame):
        return len(df)
    else:
        raise ValueError("Input is not a pandas DataFrame")

def col_count(df):
    """
    Returns the number of columns in the DataFrame.

    :param df: Pandas DataFrame.
    :return: Number of columns.
    """
    if isinstance(df, pd.DataFrame):
        return len(df.columns)
    else:
        raise ValueError("Input is not a pandas DataFrame")
