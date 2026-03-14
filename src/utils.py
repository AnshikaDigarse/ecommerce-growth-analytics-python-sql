"""
Utility helper functions used across the project.
"""

import pandas as pd


def save_dataframe(df, path):

    df.to_csv(path, index=False)


def load_dataframe(path):

    return pd.read_csv(path)

