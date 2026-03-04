import pandas as pd
import numpy as np


class CartEngine:
    """
    Simulates add-to-cart events from sessions.
    Calibrated for realistic industry-level conversion rates (~22–25%).
    """

    def __init__(self, sessions_df, customers_df, latent_traits_df, products_df):
        self.sessions = sessions_df
        self.customers = customers_df
        self.latent = latent_traits_df
        self.products = products_df
        self.cart_events = None

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

    def generate_cart_events(self):

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
                    replace=True
                )

                for _, product in selected_products.iterrows():

                    quantity = np.random.randint(1, 3)

                    cart_records.append([
                        cart_id,
                        row["session_id"],
                        row["customer_id"],
                        product["product_id"],
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
                "quantity"
            ]
        )

        return self.cart_events