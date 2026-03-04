# Customer engine logic
import pandas as pd
import numpy as np
from datetime import timedelta
from .config import (
    NUM_CUSTOMERS,
    SIMULATION_START,
    SIMULATION_END,
    CHANNELS,
    REGIONS,
    DEVICES,
    AB_SPLIT
)

class CustomerEngine:
    """
    CustomerEngine is responsible for generating
    customer dimension table and latent behavioral traits.
    """

    def __init__(self):
        self.customers = None
        self.latent_traits = None

    def generate_customers(self):
        """
        Generates observable customer dimension table.
        """

        customer_ids = np.arange(1, NUM_CUSTOMERS + 1)

        # Signup dates with slight growth trend
        date_range = pd.date_range(SIMULATION_START, SIMULATION_END)
        growth_weights = np.linspace(1, 2, len(date_range))
        growth_weights /= growth_weights.sum()

        signup_dates = np.random.choice(
            date_range,
            size=NUM_CUSTOMERS,
            p=growth_weights
        )

        # Acquisition channel
        acquisition_channel = np.random.choice(
            list(CHANNELS.keys()),
            size=NUM_CUSTOMERS,
            p=list(CHANNELS.values())
        )

        # Region
        region = np.random.choice(REGIONS, size=NUM_CUSTOMERS)

        # Preferred device
        device_type = np.random.choice(
            DEVICES,
            size=NUM_CUSTOMERS,
            p=[0.6, 0.3, 0.1]  # Mobile heavy bias (realistic)
        )

        # A/B group assignment
        ab_group = np.random.choice(
            ["Control", "Treatment"],
            size=NUM_CUSTOMERS,
            p=[AB_SPLIT, 1 - AB_SPLIT]
        )

        # Marketing cost by channel (realistic CAC)
        marketing_cost_map = {
            "Paid Ads": 120,
            "Organic": 20,
            "Referral": 40,
            "Influencer": 80
        }

        marketing_cost = [
            marketing_cost_map[ch] for ch in acquisition_channel
        ]

        self.customers = pd.DataFrame({
            "customer_id": customer_ids,
            "signup_date": signup_dates,
            "acquisition_channel": acquisition_channel,
            "region": region,
            "device_type": device_type,
            "ab_group": ab_group,
            "marketing_cost": marketing_cost
        })

        return self.customers

    def generate_latent_traits(self):
        """
        Generates hidden behavioral traits.
        These are NOT exported.
        They drive behavioral simulation.
        """

        # Activity propensity (how frequently user visits)
        activity_propensity = np.clip(
            np.random.beta(2, 5, NUM_CUSTOMERS),
            0,
            1
        )

        # Price sensitivity (higher → more discount dependent)
        price_sensitivity = np.clip(
            np.random.beta(5, 2, NUM_CUSTOMERS),
            0,
            1
        )

        # Engagement level (affects cart + conversion)
        engagement_level = np.clip(
            np.random.normal(0.6, 0.15, NUM_CUSTOMERS),
            0,
            1
        )

        self.latent_traits = pd.DataFrame({
            "customer_id": np.arange(1, NUM_CUSTOMERS + 1),
            "activity_propensity": activity_propensity,
            "price_sensitivity": price_sensitivity,
            "engagement_level": engagement_level
        })

        return self.latent_traits