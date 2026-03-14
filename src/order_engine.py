import pandas as pd
import numpy as np
from src.customer_engine import CustomerEngine


class OrderEngine:
    """
    Converts cart items into finalized orders using
    item-level probabilistic modeling.

    Features:
    - Partial cart conversion
    - Parameterized discount ranges
    - Channel effects
    - Price sensitivity impact
    - Full margin economics
    """

    def __init__(
        self,
        cart_df,
        sessions_df,
        customers_df,
        products_df,
        treatment_discount_range=(0.20, 0.50),
        control_discount_range=(0.00, 0.10),
    ):

        # Store discount ranges (this enables scenario simulation)
        self.treatment_discount_range = treatment_discount_range
        self.control_discount_range = control_discount_range

        self.cart_events = cart_df
        self.sessions = sessions_df
        self.customers = customers_df
        self.latent = CustomerEngine().generate_latent_traits()
        self.products = products_df

        # Enrich cart data
        self.cart = (
            self.cart_events
            .merge(
                self.customers[["customer_id", "ab_group", "acquisition_channel"]],
                on="customer_id",
                how="left"
            )
            .merge(
                self.latent,
                on="customer_id",
                how="left"
            )
            .merge(
                self.products,
                on="product_id",
                how="left"
            )
        )

        self.orders = None

    def generate(self):

        order_records = []
        order_id = 1

        for _, row in self.cart.iterrows():

            # ---------------------------
            # Base Cart → Purchase Rate
            # ---------------------------
            purchase_prob = 0.70

            # Engagement boost
            purchase_prob *= (1 + row["engagement_level"] * 0.15)

            # Price sensitivity penalty (Control only)
            if row["ab_group"] == "Control":
                purchase_prob *= (1 - row["price_sensitivity"] * 0.25)

            # Channel multiplier
            channel_multiplier = {
                "Organic": 1.05,
                "Paid Ads": 1.0,
                "Referral": 1.10,
                "Influencer": 0.90
            }[row["acquisition_channel"]]

            purchase_prob *= channel_multiplier

            # High-ticket penalty
            if row["base_price"] > 30000:
                purchase_prob *= 0.85

            purchase_prob = min(purchase_prob, 0.95)

            # ---------------------------
            # Purchase Decision
            # ---------------------------
            if np.random.rand() < purchase_prob:

                # Discount logic (now parameterized)
                if row["ab_group"] == "Treatment":
                    discount_pct = np.random.uniform(
                        *self.treatment_discount_range
                    )
                else:
                    discount_pct = np.random.uniform(
                        *self.control_discount_range
                    )

                original_price = row["base_price"] * row["quantity"]
                discount_amount = original_price * discount_pct
                final_price = original_price - discount_amount

                cost = row["cost"] * row["quantity"]
                margin = final_price - cost

                order_records.append([
                    order_id,
                    row["customer_id"],
                    row["session_id"],
                    row["product_id"],
                    row["quantity"],
                    row["ab_group"],
                    row["acquisition_channel"],
                    round(original_price, 2),
                    round(discount_pct, 3),
                    round(discount_amount, 2),
                    round(final_price, 2),
                    round(cost, 2),
                    round(margin, 2)
                ])

                order_id += 1

        self.orders = pd.DataFrame(
            order_records,
            columns=[
                "order_id",
                "customer_id",
                "session_id",
                "product_id",
                "quantity",
                "ab_group",
                "acquisition_channel",
                "original_price",
                "discount_pct",
                "discount_amount",
                "final_price",
                "cost",
                "margin"
            ]
        )

        self.orders.to_csv("data/raw/orders.csv", index=False)

        return self.orders