# generate_cart_events.py

import pandas as pd
import numpy as np


def generate_cart_events(sessions_df, products_df):
    """
    Simulate add-to-cart events
    """

    cart_data = []
    cart_id = 1

    for _, row in sessions_df.iterrows():

        # Higher engagement → higher chance
        prob = 0.15 + (row["pages_viewed"] / 100)

        if np.random.rand() < prob:

            num_items = np.random.randint(1, 4)

            sampled_products = products_df.sample(num_items, replace=True)

            for _, product in sampled_products.iterrows():

                cart_data.append([
                    cart_id,
                    row["session_id"],
                    row["customer_id"],
                    product["product_id"],
                    np.random.randint(1, 3),
                    "add_to_cart",
                    row["session_date"]
                ])

                cart_id += 1

    return pd.DataFrame(cart_data, columns=[
        "cart_id", "session_id", "customer_id",
        "product_id", "quantity", "event_type", "event_timestamp"
    ])