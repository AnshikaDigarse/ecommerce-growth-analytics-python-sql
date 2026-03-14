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

from src.customer_engine import CustomerEngine
from src.product_engine import ProductEngine
from src.session_engine import SessionEngine
from src.cart_engine import CartEngine
from src.order_engine import OrderEngine
from src.etl_pipeline import ETLPipeline

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

    customers = CustomerEngine().generate()
    print("Customers generated")

    # Generate and save latent traits
    latent_traits = CustomerEngine().generate_latent_traits()
    latent_traits.to_csv("data/processed/customer_latent_traits.csv", index=False)
    print("Latent traits generated")

    products = ProductEngine().generate()
    print("Products generated")

    sessions = SessionEngine(customers).generate()
    print("Sessions generated")

    cart_events = CartEngine(sessions, products).generate()
    print("Cart events generated")

    orders = OrderEngine(
        cart_events,
        sessions,
        customers,
        products
    ).generate()

    print("Orders generated")

    print("Running ETL pipeline")

    etl = ETLPipeline()
    etl.run()

    print("ETL completed")

    build_star_schema()

    print("Pipeline finished successfully")


if __name__ == "__main__":
    main()