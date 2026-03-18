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
    "Electronics": 0.10,
    "Fashion": 0.30,
    "Home": 0.40,
    "Beauty": 0.45,
    "Grocery": 0.08
}


CATEGORY_PRICE_RANGE = {

    "Electronics": (1000, 200000),

    "Fashion": (500, 20000),

    "Home": (800, 25000),

    "Beauty": (200, 30000),

    "Grocery": (50, 2500)
}

# Seasonality Parameters
FESTIVE_MONTH = 11
SLOW_MONTH = 8

WEEKEND_BOOST = 1.10
FESTIVE_BOOST = 1.25
SLOW_MONTH_DROP = 0.85

# Database Configuration
DATABASE_URL = "mysql+pymysql://root:Anshika%401@localhost:3306/ecommerce_analytics"