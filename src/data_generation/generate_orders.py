# generate_orders.py

import pandas as pd
import numpy as np


def generate_orders(cart_df, products_df):
    """
    Converts cart items into final orders
    """

    orders = []
    order_id = 1

    merged = cart_df.merge(products_df, on="product_id")

    for _, row in merged.iterrows():

        if np.random.rand() < 0.7:

            total_price = row["base_price"] * row["quantity"]

            orders.append([
                order_id,
                row["customer_id"],
                row["session_id"],
                total_price
            ])

            order_id += 1

    return pd.DataFrame(orders, columns=[
        "order_id", "customer_id", "session_id", "revenue"
    ])