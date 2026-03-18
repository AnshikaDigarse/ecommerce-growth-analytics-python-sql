# etl_pipeline.py

import pandas as pd


def run_etl():
    """
    Basic ETL:
    - Read raw data
    - Save processed data
    """

    customers = pd.read_csv("data/raw/customers.csv")
    orders = pd.read_csv("data/raw/orders.csv")

    # simple cleaning
    orders = orders.drop_duplicates()

    customers.to_csv("data/processed/customers.csv", index=False)
    orders.to_csv("data/processed/orders.csv", index=False)

    print("ETL completed")