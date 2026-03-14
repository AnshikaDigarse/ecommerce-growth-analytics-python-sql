import pandas as pd
import numpy as np
from src.customer_engine import CustomerEngine


class CartEngine:
    """
    Simulates add-to-cart events from sessions.
    Calibrated for realistic industry-level conversion rates (~22–25%).
    """

    def __init__(self, sessions_df, products_df):

        self.sessions = sessions_df
        self.products = products_df
        self.cart_events = None

        self.customers = CustomerEngine().generate()
        self.latent = CustomerEngine().generate_latent_traits()

        # Merge necessary behavioral data once (efficient)
        self.sessions = self.sessions.merge(
            self.customers[["customer_id", "acquisition_channel", "ab_group"]],
            on="customer_id",
            how="left"
        ).merge(
            self.latent,
            on="customer_id",
            how="left"
        )

    def generate(self):

        cart_records = []
        cart_id = 1

        for _, row in self.sessions.iterrows():

            # -------------------------------
            # BASE CONVERSION RATE (Reduced)
            # -------------------------------
            base_prob = 0.14   # reduced from 0.18

            # -------------------------------
            # Engagement Effect (Reduced)
            # -------------------------------
            engagement_effect = row["engagement_level"] * 0.20
            base_prob *= (1 + engagement_effect)

            # -------------------------------
            # Browsing Effect (Slightly Reduced)
            # -------------------------------
            browsing_effect = min(row["pages_viewed"] / 15, 0.4)
            base_prob *= (1 + browsing_effect)

            # -------------------------------
            # Bounce Penalty (Stronger)
            # -------------------------------
            if row["bounced_flag"] == 1:
                base_prob *= 0.20

            # -------------------------------
            # Channel Adjustment
            # -------------------------------
            channel_multiplier = {
                "Organic": 1.05,
                "Paid Ads": 1.0,
                "Referral": 1.10,
                "Influencer": 0.80
            }[row["acquisition_channel"]]

            base_prob *= channel_multiplier

            # -------------------------------
            # Treatment Uplift (More Realistic)
            # -------------------------------
            if row["ab_group"] == "Treatment":
                base_prob *= 1.05   # reduced from 1.08

            # Safety cap
            base_prob = min(base_prob, 0.75)

            # -------------------------------
            # Conversion Decision
            # -------------------------------
            if np.random.rand() < base_prob:

                # Basket size: skewed realistic distribution
                basket_size = min(np.random.poisson(2) + 1, 7)

                selected_products = self.products.sample(
                    basket_size,
                    replace=True,
                    random_state=42
                )

                for _, product in selected_products.iterrows():

                    quantity = np.random.randint(1, 3)

                    event_timestamp = pd.to_datetime(row["session_date"]) + pd.to_timedelta(np.random.randint(0, 1440), unit="m")
                    cart_records.append([
                        cart_id,
                        row["session_id"],
                        row["customer_id"],
                        product["product_id"],
                        "add_to_cart",
                        event_timestamp,
                        quantity
                    ])

                    cart_id += 1

        self.cart_events = pd.DataFrame(
            cart_records,
            columns=[
                "cart_id",
                "session_id",
                "customer_id",
                "product_id",
                "event_type",
                "event_timestamp",
                "quantity"
            ]
        )

        self.cart_events.to_csv("data/raw/cart_events.csv", index=False)

        return self.cart_events