import pandas as pd
import numpy as np

from src.config import NUM_PRODUCTS, CATEGORY_MARGIN, CATEGORY_PRICE_RANGE


class ProductEngine:

    def generate(self):

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

        products = pd.DataFrame(data)

        products.to_csv("data/raw/products.csv", index=False)

        return products