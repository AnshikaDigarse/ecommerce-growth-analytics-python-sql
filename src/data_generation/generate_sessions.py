# generate_sessions.py

import pandas as pd
import numpy as np
from src.core.config import SIMULATION_START, SIMULATION_END, DEVICES


def generate_sessions(customers_df):
    """
    Simulate user browsing behavior
    """

    sessions = []
    session_id = 1

    date_range = pd.date_range(SIMULATION_START, SIMULATION_END)

    for _, row in customers_df.iterrows():

        num_sessions = np.random.poisson(5)

        for _ in range(num_sessions):

            pages = np.random.randint(1, 12)
            duration = np.random.randint(30, 900)

            sessions.append([
                session_id,
                row["customer_id"],
                np.random.choice(date_range),
                np.random.choice(DEVICES),
                row["acquisition_channel"],
                pages,
                duration,
                1 if pages <= 1 else 0
            ])

            session_id += 1

    return pd.DataFrame(sessions, columns=[
        "session_id", "customer_id", "session_date",
        "device", "traffic_source",
        "pages_viewed", "session_duration", "bounced_flag"
    ])