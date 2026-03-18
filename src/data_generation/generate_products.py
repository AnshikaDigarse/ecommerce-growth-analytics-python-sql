# generate_products.py

import pandas as pd
import numpy as np
from src.core.config import NUM_PRODUCTS, CATEGORY_MARGIN, CATEGORY_PRICE_RANGE


def generate_products():
    """
    Generates product catalog with pricing and margins
    """

    categories = list(CATEGORY_MARGIN.keys())
    data = []

    for i in range(NUM_PRODUCTS):
        category = np.random.choice(categories)
        margin = CATEGORY_MARGIN[category]
        min_price, max_price = CATEGORY_PRICE_RANGE[category]

        price = np.random.uniform(min_price, max_price)
        cost = price * (1 - margin)

        data.append({
            "product_id": i + 1,
            "category": category,
            "base_price": round(price, 2),
            "cost": round(cost, 2)
        })

    return pd.DataFrame(data)