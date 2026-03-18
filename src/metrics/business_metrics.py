# Metrics engine logic
import pandas as pd
import numpy as np


class MetricsEngine:
    """
    Centralized KPI calculation layer.
    Ensures consistent metric definitions across notebooks and dashboards.
    """

    def __init__(self, sessions_df, orders_df):
        self.sessions = sessions_df.copy()
        self.orders = orders_df.copy()

    # -----------------------------
    # Funnel Metrics
    # -----------------------------

    def conversion_rate(self):
        converted_sessions = self.orders["session_id"].nunique()
        total_sessions = self.sessions["session_id"].nunique()
        return converted_sessions / total_sessions

    def conversion_by_group(self):
        merged = self.sessions.merge(
            self.orders[["session_id"]].drop_duplicates(),
            on="session_id",
            how="left",
            indicator=True
        )

        merged["converted"] = (merged["_merge"] == "both").astype(int)

        return merged.groupby("ab_group")["converted"].mean()

    # -----------------------------
    # Revenue Metrics
    # -----------------------------

    def average_order_value(self):
        return self.orders.groupby("ab_group")["final_price"].mean()

    def total_revenue(self):
        return self.orders.groupby("ab_group")["final_price"].sum()

    # -----------------------------
    # Margin Metrics
    # -----------------------------

    def average_margin(self):
        return self.orders.groupby("ab_group")["margin"].mean()

    def total_margin(self):
        return self.orders.groupby("ab_group")["margin"].sum()

    # -----------------------------
    # Customer LTV
    # -----------------------------

    def customer_ltv(self):
        return (
            self.orders
            .groupby(["customer_id", "ab_group"])["final_price"]
            .sum()
            .groupby("ab_group")
            .mean()
        )

    def customer_margin_ltv(self):
        return (
            self.orders
            .groupby(["customer_id", "ab_group"])["margin"]
            .sum()
            .groupby("ab_group")
            .mean()
        )