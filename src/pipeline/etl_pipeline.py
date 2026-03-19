import pandas as pd
from sqlalchemy import create_engine
from src.core.config import DATABASE_URL


def run_etl():
    print("🔄 Running ETL...")

    # -----------------------
    # EXTRACT
    # -----------------------
    customers = pd.read_csv("data/raw/customers.csv")
    sessions = pd.read_csv("data/raw/sessions.csv")
    orders = pd.read_csv("data/raw/orders.csv")
    products = pd.read_csv("data/raw/products.csv")
    cart_events = pd.read_csv("data/raw/cart_events.csv")

    # -----------------------
    # TRANSFORM
    # -----------------------
    sessions["session_date"] = pd.to_datetime(sessions["session_date"])
    orders["order_date"] = pd.to_datetime(orders["order_date"])

    orders = orders.drop_duplicates()

    # -----------------------
    # LOAD TO CSV (processed)
    # -----------------------
    customers.to_csv("data/processed/customers.csv", index=False)
    sessions.to_csv("data/processed/sessions.csv", index=False)
    orders.to_csv("data/processed/orders.csv", index=False)
    products.to_csv("data/processed/products.csv", index=False)
    cart_events.to_csv("data/processed/cart_events.csv", index=False)

    # -----------------------
    # LOAD TO MYSQL
    # -----------------------
    print("📦 Loading into MySQL...")

    engine = create_engine(DATABASE_URL)

    customers.to_sql("customers", engine, if_exists="replace", index=False)
    sessions.to_sql("sessions", engine, if_exists="replace", index=False)
    orders.to_sql("orders", engine, if_exists="replace", index=False)
    products.to_sql("products", engine, if_exists="replace", index=False)
    cart_events.to_sql("cart_events", engine, if_exists="replace", index=False)

    print("✅ ETL + MySQL Load Completed")