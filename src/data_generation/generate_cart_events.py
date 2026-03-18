# generate_cart_events.py

import pandas as pd
import numpy as np


def generate_cart_events(sessions_df, products_df):
    """
    Simulates add-to-cart events
    """

    cart_data = []
    cart_id = 1

    for _, row in sessions_df.iterrows():

        # simple probability
        if np.random.rand() < 0.2:

            product = products_df.sample(1).iloc[0]

            cart_data.append([
                cart_id,
                row["session_id"],
                row["customer_id"],
                product["product_id"],
                np.random.randint(1, 3)
            ])

            cart_id += 1

    return pd.DataFrame(cart_data, columns=[
        "cart_id", "session_id", "customer_id",
        "product_id", "quantity"
    ])