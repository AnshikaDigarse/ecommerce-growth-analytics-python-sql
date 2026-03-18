# generate_customers.py

import pandas as pd
import numpy as np
from src.core.config import NUM_CUSTOMERS, CHANNELS, AB_SPLIT


def generate_customers():
    """
    Generates basic customer dataset
    """

    customers = pd.DataFrame({
        "customer_id": range(1, NUM_CUSTOMERS + 1),
        "acquisition_channel": np.random.choice(
            list(CHANNELS.keys()),
            NUM_CUSTOMERS
        )
    })

    # Assign A/B group
    customers["ab_group"] = np.where(
        np.random.rand(NUM_CUSTOMERS) < AB_SPLIT,
        "Treatment",
        "Control"
    )

    return customers