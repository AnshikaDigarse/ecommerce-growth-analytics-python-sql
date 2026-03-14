import pandas as pd
import numpy as np

from src.config import NUM_CUSTOMERS, CHANNELS, AB_SPLIT


class CustomerEngine:

    def generate(self):

        customers = pd.DataFrame({

            "customer_id": range(1, NUM_CUSTOMERS + 1),

            "acquisition_channel": np.random.choice(
                list(CHANNELS.keys()),
                NUM_CUSTOMERS
            )

        })

        customers["ab_group"] = np.where(

            np.random.rand(NUM_CUSTOMERS) < AB_SPLIT,
            "Treatment",
            "Control"

        )

        customers.to_csv("data/raw/customers.csv", index=False)

        return customers


    def generate_latent_traits(self):

        """
        Generate hidden behavioral traits for each customer.
        These traits influence session behavior and purchasing decisions.
        """

        latent = pd.DataFrame({

            "customer_id": range(1, NUM_CUSTOMERS + 1),

            "activity_propensity": np.random.beta(2,2,NUM_CUSTOMERS),

            "price_sensitivity": np.random.beta(2,5,NUM_CUSTOMERS),

            "engagement_level": np.random.beta(3,2,NUM_CUSTOMERS)

        })

        return latent