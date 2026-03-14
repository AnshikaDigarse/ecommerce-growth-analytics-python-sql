import pandas as pd
import numpy as np
from src.customer_engine import CustomerEngine

from src.config import (
    SIMULATION_START,
    SIMULATION_END,
    WEEKEND_BOOST,
    FESTIVE_MONTH,
    SLOW_MONTH,
    FESTIVE_BOOST,
    SLOW_MONTH_DROP,
    DEVICES
)


class SessionEngine:
    """
    Optimized session generation engine.

    Generates sessions per customer using probabilistic modeling.
    Avoids nested day × customer loops for performance efficiency.
    """

    def __init__(self, customers_df):

        self.latent = CustomerEngine().generate_latent_traits()

        # Merge latent traits once (critical optimization)
        self.customers = customers_df.merge(
            self.latent,
            on="customer_id",
            how="left"
        )
        self.sessions = None

    def generate(self):

        date_range = pd.date_range(SIMULATION_START, SIMULATION_END)

        session_records = []
        session_id = 1

        for _, row in self.customers.iterrows():

            customer_id = row["customer_id"]
            channel = row["acquisition_channel"]
            ab_group = row["ab_group"]
            activity_propensity = row["activity_propensity"]

            # ---------------------------------------------------
            # Base session intensity (6 month expectation)
            # ---------------------------------------------------
            base_intensity = activity_propensity * 15

            # Channel behavior multiplier
            channel_multiplier = {
                "Organic": 1.1,
                "Paid Ads": 1.0,
                "Referral": 1.2,
                "Influencer": 0.9
            }[channel]

            base_intensity *= channel_multiplier

            # Treatment increases engagement slightly
            if ab_group == "Treatment":
                base_intensity *= 1.05

            # Generate session count using Poisson distribution
            num_sessions = np.random.poisson(base_intensity)

            if num_sessions <= 0:
                continue

            # Randomly assign session dates
            session_dates = np.random.choice(date_range, size=num_sessions)

            for date in session_dates:

                date = pd.Timestamp(date)
                month = date.month
                is_weekend = date.weekday() >= 5

                seasonal_multiplier = 1

                if month == FESTIVE_MONTH:
                    seasonal_multiplier *= FESTIVE_BOOST
                elif month == SLOW_MONTH:
                    seasonal_multiplier *= SLOW_MONTH_DROP

                if is_weekend:
                    seasonal_multiplier *= WEEKEND_BOOST

                # Pages viewed influenced by seasonal intensity
                pages_viewed = max(
                    1,
                    int(np.random.poisson(4 * seasonal_multiplier))
                )

                # Session duration in seconds
                session_duration = max(
                    30,
                    int(np.random.normal(300, 80))
                )

                bounced_flag = 1 if pages_viewed <= 1 else 0

                session_records.append([
                    session_id,
                    customer_id,
                    date,
                    np.random.choice(DEVICES),
                    channel,
                    pages_viewed,
                    session_duration,
                    bounced_flag
                ])

                session_id += 1

        self.sessions = pd.DataFrame(
            session_records,
            columns=[
                "session_id",
                "customer_id",
                "session_date",
                "device_type",
                "traffic_source",
                "pages_viewed",
                "session_duration",
                "bounced_flag"
            ]
        )

        self.sessions.to_csv("data/raw/sessions.csv", index=False)

        return self.sessions