"""
Main pipeline runner for E-commerce Growth Analytics Platform

Flow:
1. Generate raw data
2. Save raw data
3. Run ETL pipeline
4. Build data warehouse (star schema)
"""

import os
from sqlalchemy import create_engine, text

# Data generation
from src.data_generation.generate_customers import generate_customers
from src.data_generation.generate_products import generate_products
from src.data_generation.generate_sessions import generate_sessions
from src.data_generation.generate_cart_events import generate_cart_events
from src.data_generation.generate_orders import generate_orders

# Pipeline
from src.pipeline.etl_pipeline import run_etl

# Utilities
from src.core.utils import save_dataframe
from src.core.config import DATABASE_URL


# -----------------------------
# STEP 1: DATA GENERATION
# -----------------------------
def generate_all_data():
    print("\n📦 Generating Data...")

    customers = generate_customers()
    save_dataframe(customers, "data/raw/customers.csv")

    products = generate_products()
    save_dataframe(products, "data/raw/products.csv")

    sessions = generate_sessions(customers)
    save_dataframe(sessions, "data/raw/sessions.csv")

    cart_events = generate_cart_events(sessions, products)
    save_dataframe(cart_events, "data/raw/cart_events.csv")

    orders = generate_orders(cart_events, products)
    save_dataframe(orders, "data/raw/orders.csv")

    print("✅ Data Generation Completed\n")


# -----------------------------
# STEP 2: BUILD STAR SCHEMA
# -----------------------------
def build_star_schema():
    print("🏗️ Building Star Schema...")

    engine = create_engine(DATABASE_URL)

    base_path = os.path.dirname(os.path.abspath(__file__))
    sql_file = os.path.join(base_path, "sql", "star_schema.sql")

    with open(sql_file, "r") as file:
        sql_script = file.read()

    with engine.connect() as conn:
        for statement in sql_script.split(";"):
            stmt = statement.strip()
            if stmt:
                conn.execute(text(stmt))

    print("✅ Star Schema Created\n")


# -----------------------------
# MAIN FUNCTION
# -----------------------------
def main():
    print("🚀 Starting E-commerce Analytics Pipeline\n")

    # Ensure correct working directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # 1. Generate Data
    generate_all_data()

    # 2. Run ETL
    print("🔄 Running ETL Pipeline...")
    run_etl()
    print("✅ ETL Completed\n")

    # 3. Build Warehouse
    build_star_schema()

    print("🎉 Pipeline Completed Successfully")


# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    main()