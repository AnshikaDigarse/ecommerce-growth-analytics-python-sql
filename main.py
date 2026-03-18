"""
Main pipeline runner for the E-commerce Growth Analytics Platform.

Pipeline steps
--------------
1. Generate simulated datasets
2. Save raw CSV files
3. Run ETL pipeline
4. Build SQL warehouse (star schema)
"""

import os

from src.data_generation.generate_customers import generate_customers
from src.data_generation.generate_products import generate_products
from src.data_generation.generate_sessions import generate_sessions
from src.data_generation.generate_cart_events import generate_cart_events
from src.data_generation.generate_orders import generate_orders
from src.pipeline.etl_pipeline import run_etl
from src.core.utils import save_dataframe

from sqlalchemy import create_engine, text


def build_star_schema():

    print("Building warehouse star schema...")

    engine = create_engine(
        "mysql+pymysql://root:Anshika%401@localhost:3306/ecommerce_analytics"
    )

    base_path = os.path.dirname(os.path.abspath(__file__))
    sql_file = os.path.join(base_path, "sql", "star_schema.sql")

    with open(sql_file, "r") as file:
        sql_script = file.read()

    with engine.connect() as conn:
        for statement in sql_script.split(";"):
            stmt = statement.strip()
            if stmt:
                conn.execute(text(stmt))

    print("Star schema created successfully.")


def main():
    # Change to the script's directory to ensure relative paths work
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print("Starting E-commerce Growth Platform Simulation")

    customers = generate_customers()
    save_dataframe(customers, "data/raw/customers.csv")
    print("Customers generated")

    products = generate_products()
    save_dataframe(products, "data/raw/products.csv")
    print("Products generated")

    sessions = generate_sessions(customers)
    save_dataframe(sessions, "data/raw/sessions.csv")
    print("Sessions generated")

    cart_events = generate_cart_events(sessions, products)
    save_dataframe(cart_events, "data/raw/cart_events.csv")
    print("Cart events generated")

    orders = generate_orders(cart_events, products)
    save_dataframe(orders, "data/raw/orders.csv")
    print("Orders generated")

    print("Running ETL pipeline")

    run_etl()

    print("ETL completed")

    build_star_schema()

    print("Pipeline finished successfully")


if __name__ == "__main__":
    main()