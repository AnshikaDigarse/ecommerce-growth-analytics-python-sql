"""
ETL pipeline that loads raw CSV data into MySQL.
"""

import pandas as pd
import os
from sqlalchemy import create_engine


class ETLPipeline:

    def __init__(self):

        self.engine = create_engine(
            "mysql+pymysql://root:Anshika%401@localhost:3306/ecommerce_analytics"
        )

        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        raw_path = os.path.join(base_path, "data", "raw")

        self.paths = {
            "customers": os.path.join(raw_path, "customers.csv"),
            "sessions": os.path.join(raw_path, "sessions.csv"),
            "orders": os.path.join(raw_path, "orders.csv"),
            "products": os.path.join(raw_path, "products.csv"),
            "cart_events": os.path.join(raw_path, "cart_events.csv"),
        }

    def extract(self):

        print("Extracting data")

        self.customers = pd.read_csv(self.paths["customers"])
        self.sessions = pd.read_csv(self.paths["sessions"])
        self.orders = pd.read_csv(self.paths["orders"])
        self.products = pd.read_csv(self.paths["products"])
        self.cart_events = pd.read_csv(self.paths["cart_events"])

    def transform(self):

        print("Transforming data")

        if "session_date" in self.sessions.columns:
            self.sessions["session_date"] = pd.to_datetime(self.sessions["session_date"])

    def load(self):

        print("Loading data into MySQL")

        self.customers.to_sql("customers", self.engine, if_exists="replace", index=False)
        self.sessions.to_sql("sessions", self.engine, if_exists="replace", index=False)
        self.orders.to_sql("orders", self.engine, if_exists="replace", index=False)
        self.products.to_sql("products", self.engine, if_exists="replace", index=False)
        self.cart_events.to_sql("cart_events", self.engine, if_exists="replace", index=False)

        print("Tables loaded successfully")

    def run(self):

        self.extract()
        self.transform()
        self.load()