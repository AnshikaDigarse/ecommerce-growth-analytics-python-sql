# generate_customers.py

import pandas as pd
import numpy as np
from src.core.config import NUM_CUSTOMERS, CHANNELS, AB_SPLIT, SIMULATION_START, SIMULATION_END


def generate_customers():
    """
    Generate customer profiles with acquisition and signup info
    """

    date_range = pd.date_range(SIMULATION_START, SIMULATION_END)

    customers = pd.DataFrame({
        "customer_id": range(1, NUM_CUSTOMERS + 1),
        "acquisition_channel": np.random.choice(
            list(CHANNELS.keys()),
            NUM_CUSTOMERS
        ),
        "signup_date": np.random.choice(date_range, NUM_CUSTOMERS)
    })

    # Assign A/B group
    customers["ab_group"] = np.where(
        np.random.rand(NUM_CUSTOMERS) < AB_SPLIT,
        "Treatment",
        "Control"
    )

    return customers