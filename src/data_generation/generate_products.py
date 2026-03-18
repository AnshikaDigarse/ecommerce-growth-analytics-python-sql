# generate_products.py

import pandas as pd
import numpy as np
from src.core.config import NUM_PRODUCTS, CATEGORY_MARGIN, CATEGORY_PRICE_RANGE


def generate_products():
    """
    Generate realistic product catalog with pricing and cost structure
    """

    products = []

    categories = list(CATEGORY_MARGIN.keys())

    for i in range(NUM_PRODUCTS):

        category = np.random.choice(categories)

        min_price, max_price = CATEGORY_PRICE_RANGE[category]
        base_price = np.random.uniform(min_price, max_price)

        margin_pct = CATEGORY_MARGIN[category]
        cost = base_price * (1 - margin_pct)

        products.append([
            i + 1,
            category,
            round(base_price, 2),
            round(cost, 2),
            margin_pct
        ])

    return pd.DataFrame(products, columns=[
        "product_id", "category", "base_price", "cost", "margin_pct"
    ])