"""
Global configuration for simulation.
"""

import numpy as np
import random

RANDOM_SEED = 42

np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)


NUM_CUSTOMERS = 2500
NUM_PRODUCTS = 120

SIMULATION_START = "2025-07-01"
SIMULATION_END = "2025-12-31"


AB_SPLIT = 0.5


CHANNELS = {
    "Paid Ads": 0.4,
    "Organic": 0.4,
    "Referral": 0.1,
    "Influencer": 0.1
}


DEVICES = ["Mobile", "Desktop", "Tablet"]


CATEGORY_MARGIN = {
    "Electronics": 0.15,
    "Fashion": 0.50,
    "Home": 0.35,
    "Beauty": 0.60,
    "Grocery": 0.15
}


CATEGORY_PRICE_RANGE = {

    "Electronics": (1000, 50000),

    "Fashion": (500, 10000),

    "Home": (800, 50000),

    "Beauty": (200, 25000),

    "Grocery": (50, 5000)
}

# Seasonality Parameters
FESTIVE_MONTH = 11
SLOW_MONTH = 8

WEEKEND_BOOST = 1.10
FESTIVE_BOOST = 1.45
SLOW_MONTH_DROP = 0.80

# Database Configuration
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get DB connection from .env
DATABASE_URL = os.getenv("DATABASE_URL")