# generate_sessions.py

import pandas as pd
import numpy as np
from src.core.config import SIMULATION_START, SIMULATION_END, DEVICES


def generate_sessions(customers_df):
    """
    Simulates user sessions (website visits)
    """

    date_range = pd.date_range(SIMULATION_START, SIMULATION_END)
    sessions = []

    session_id = 1

    for _, row in customers_df.iterrows():

        num_sessions = np.random.randint(1, 20)

        for _ in range(num_sessions):

            sessions.append([
                session_id,
                row["customer_id"],
                np.random.choice(date_range),
                np.random.choice(DEVICES),
                np.random.randint(1, 10),   # pages viewed
                np.random.randint(30, 600) # duration
            ])

            session_id += 1

    return pd.DataFrame(sessions, columns=[
        "session_id", "customer_id", "session_date",
        "device", "pages_viewed", "session_duration"
    ])