from pathlib import Path

from src.customer_engine import CustomerEngine
from src.product_engine import ProductEngine
from src.session_engine import SessionEngine
from src.cart_engine import CartEngine


# -------------------------------------------------
# Resolve project root based on file location
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_RAW = BASE_DIR / "data" / "raw"
DATA_PROCESSED = BASE_DIR / "data" / "processed"


def ensure_directories():
    DATA_RAW.mkdir(parents=True, exist_ok=True)
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)


def main():

    print("Starting E-commerce Growth Platform Simulation...")
    ensure_directories()

    # Customers
    customer_engine = CustomerEngine()
    customers = customer_engine.generate_customers()
    latent_traits = customer_engine.generate_latent_traits()

    customers.to_csv(DATA_RAW / "customers.csv", index=False)
    latent_traits.to_csv(DATA_PROCESSED / "customer_latent_traits.csv", index=False)

    print("Customers generated.")

    # Products
    product_engine = ProductEngine()
    products = product_engine.generate_products()
    products.to_csv(DATA_RAW / "products.csv", index=False)

    print("Products generated.")

    # Sessions
    session_engine = SessionEngine(customers, latent_traits)
    sessions = session_engine.generate_sessions()
    sessions.to_csv(DATA_RAW / "sessions.csv", index=False)

    print(f"Sessions generated: {len(sessions)}")
    print("Simulation complete.")

    # -----------------------------------
    # Cart Events
    # -----------------------------------
    cart_engine = CartEngine(sessions, customers, latent_traits, products)
    cart_events = cart_engine.generate_cart_events()

    cart_events.to_csv(DATA_RAW / "cart_events.csv", index=False)

    print(f"Cart events generated: {len(cart_events)}")


if __name__ == "__main__":
    main()