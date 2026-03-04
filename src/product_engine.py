# Product engine logic
import pandas as pd
import numpy as np

from .config import (
    NUM_PRODUCTS,
    CATEGORY_MARGIN
)


class ProductEngine:
    """
    Responsible for generating product dimension table.
    Includes pricing and margin structure.
    """

    def __init__(self):
        self.products = None

    def generate_products(self):
        """
        Generates product dimension table with
        category-level economic realism.
        """

        product_ids = np.arange(1, NUM_PRODUCTS + 1)

        categories = list(CATEGORY_MARGIN.keys())

        # Distribute products across categories evenly
        category_assignment = np.random.choice(
            categories,
            size=NUM_PRODUCTS
        )

        base_prices = []
        margin_pct = []
        cost = []

        for cat in category_assignment:

            # -------------------------------
            # Category-specific price bands
            # -------------------------------
            if cat == "Electronics":
                price = np.random.uniform(15000, 80000)

            elif cat == "Fashion":
                price = np.random.uniform(800, 6000)

            elif cat == "Home":
                price = np.random.uniform(2000, 25000)

            elif cat == "Beauty":
                price = np.random.uniform(300, 5000)

            elif cat == "Grocery":
                price = np.random.uniform(50, 1500)

            # -------------------------------
            # Margin structure
            # -------------------------------
            base_margin = CATEGORY_MARGIN[cat]

            # Add slight noise to margin (realistic variation)
            margin = np.clip(
                np.random.normal(base_margin, 0.03),
                0.02,
                0.8
            )

            product_cost = price * (1 - margin)

            base_prices.append(round(price, 2))
            margin_pct.append(round(margin, 3))
            cost.append(round(product_cost, 2))

        self.products = pd.DataFrame({
            "product_id": product_ids,
            "category": category_assignment,
            "base_price": base_prices,
            "margin_pct": margin_pct,
            "cost": cost
        })

        return self.products