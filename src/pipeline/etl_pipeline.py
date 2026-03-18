# etl_pipeline.py

import pandas as pd


def run_etl():
    print("Extracting data...")

    customers = pd.read_csv("data/raw/customers.csv")
    sessions = pd.read_csv("data/raw/sessions.csv")
    orders = pd.read_csv("data/raw/orders.csv")
    products = pd.read_csv("data/raw/products.csv")
    cart_events = pd.read_csv("data/raw/cart_events.csv")

    print("Transforming data...")

    # Example cleaning
    sessions["session_date"] = pd.to_datetime(sessions["session_date"])
    orders = orders.drop_duplicates()

    print("Loading processed data...")

    customers.to_csv("data/processed/customers.csv", index=False)
    sessions.to_csv("data/processed/sessions.csv", index=False)
    orders.to_csv("data/processed/orders.csv", index=False)
    products.to_csv("data/processed/products.csv", index=False)
    cart_events.to_csv("data/processed/cart_events.csv", index=False)

    print("ETL completed")