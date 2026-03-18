# generate_orders.py

import pandas as pd
import numpy as np


def generate_orders(cart_df, products_df, customers_df):
    """
    Convert cart items into final purchases
    Includes pricing, discount, and margin logic
    """

    orders = []
    order_id = 1

    # Merge all required info
    df = (
        cart_df
        .merge(products_df, on="product_id")
        .merge(customers_df, on="customer_id")
    )

    for _, row in df.iterrows():

        # Base conversion probability
        purchase_prob = 0.6

        # Higher quantity → higher intent
        purchase_prob += row["quantity"] * 0.05

        # Channel effect
        if row["acquisition_channel"] == "Organic":
            purchase_prob *= 1.1

        if np.random.rand() < purchase_prob:

            original_price = row["base_price"] * row["quantity"]

            # Discount logic
            if row["ab_group"] == "Treatment":
                discount_pct = np.random.uniform(0.1, 0.3)
            else:
                discount_pct = np.random.uniform(0.0, 0.1)

            discount_amount = original_price * discount_pct
            final_price = original_price - discount_amount

            cost = row["cost"] * row["quantity"]
            margin = final_price - cost

            orders.append([
                order_id,
                row["customer_id"],
                row["session_id"],
                row["product_id"],
                row["quantity"],
                row["acquisition_channel"],
                row["ab_group"],
                round(original_price, 2),
                round(discount_amount, 2),
                round(final_price, 2),
                round(cost, 2),
                round(margin, 2),
                row["event_timestamp"]
            ])

            order_id += 1

    return pd.DataFrame(orders, columns=[
        "order_id", "customer_id", "session_id", "product_id",
        "quantity", "acquisition_channel", "ab_group",
        "original_price", "discount_amount", "final_price",
        "cost", "margin", "order_date"
    ])