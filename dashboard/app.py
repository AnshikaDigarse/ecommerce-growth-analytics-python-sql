import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import os
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="E-commerce Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Database connection
def get_db_connection():
    """Create database connection"""
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'ecommerce_analytics',
        'port': 3306
    }

    engine = create_engine(
        f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    )
    return engine

# Load data functions
@st.cache_data
def load_kpi_data():
    """Load key performance indicators"""
    engine = get_db_connection()
    query = """
    SELECT
        COUNT(DISTINCT s.session_id) as total_sessions,
        COUNT(DISTINCT o.order_id) as total_orders,
        ROUND(COUNT(DISTINCT o.order_id) * 100.0 / COUNT(DISTINCT s.session_id), 2) as conversion_rate,
        ROUND(SUM(o.total_amount), 2) as total_revenue,
        ROUND(AVG(o.total_amount), 2) as avg_order_value,
        COUNT(DISTINCT c.customer_id) as total_customers
    FROM fact_sessions s
    LEFT JOIN fact_orders o ON s.session_id = o.session_id
    LEFT JOIN dim_customers c ON s.customer_id = c.customer_id
    """
    return pd.read_sql(query, engine)

@st.cache_data
def load_revenue_trends():
    """Load revenue trends over time"""
    engine = get_db_connection()
    query = """
    SELECT
        d.date,
        d.month_name,
        d.year,
        COUNT(DISTINCT o.order_id) as orders,
        ROUND(SUM(o.total_amount), 2) as revenue,
        ROUND(AVG(o.total_amount), 2) as avg_order_value
    FROM dim_date d
    LEFT JOIN fact_orders o ON d.date = DATE(o.order_date)
    GROUP BY d.date, d.month_name, d.year
    ORDER BY d.date
    """
    return pd.read_sql(query, engine)

@st.cache_data
def load_product_performance():
    """Load product performance data"""
    engine = get_db_connection()
    query = """
    SELECT
        p.category,
        p.product_name,
        COUNT(oi.order_item_id) as units_sold,
        ROUND(SUM(oi.total_price), 2) as revenue,
        ROUND(AVG(oi.price), 2) as avg_price,
        ROUND(SUM(oi.total_price) * 100.0 / SUM(SUM(oi.total_price)) OVER (), 2) as revenue_share
    FROM dim_products p
    JOIN fact_order_items oi ON p.product_id = oi.product_id
    GROUP BY p.category, p.product_name
    ORDER BY revenue DESC
    LIMIT 20
    """
    return pd.read_sql(query, engine)

@st.cache_data
def load_customer_segments():
    """Load customer segmentation data"""
    engine = get_db_connection()
    query = """
    SELECT
        c.ab_group as customer_segment,
        COUNT(DISTINCT c.customer_id) as customers,
        COUNT(DISTINCT o.order_id) as orders,
        ROUND(SUM(o.total_amount), 2) as revenue,
        ROUND(AVG(o.total_amount), 2) as avg_order_value,
        ROUND(SUM(o.total_amount) * 100.0 / SUM(SUM(o.total_amount)) OVER (), 2) as revenue_share
    FROM dim_customer c
    LEFT JOIN fact_orders o ON c.customer_id = o.customer_id
    GROUP BY c.ab_group
    ORDER BY revenue DESC
    """
    return pd.read_sql(query, engine)

@st.cache_data
def load_experiment_results():
    """Load A/B test results"""
    engine = get_db_connection()
    query = """
    SELECT
        e.experiment_name,
        e.variant,
        COUNT(DISTINCT s.session_id) as sessions,
        COUNT(DISTINCT o.order_id) as orders,
        ROUND(COUNT(DISTINCT o.order_id) * 100.0 / COUNT(DISTINCT s.session_id), 2) as conversion_rate,
        ROUND(SUM(o.total_amount), 2) as revenue,
        ROUND(AVG(o.total_amount), 2) as avg_order_value
    FROM fact_sessions s
    LEFT JOIN fact_orders o ON s.session_id = o.session_id
    LEFT JOIN dim_experiments e ON s.experiment_id = e.experiment_id
    GROUP BY e.experiment_name, e.variant
    ORDER BY e.experiment_name, e.variant
    """
    return pd.read_sql(query, engine)

# Main dashboard
def main():
    st.title("📊 E-commerce Analytics Dashboard")
    st.markdown("---")

    # Sidebar
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Select Page", [
        "Overview",
        "Revenue Analytics",
        "Product Performance",
        "Customer Insights",
        "Experiment Results"
    ])

    # Load data
    try:
        if page == "Overview":
            show_overview()
        elif page == "Revenue Analytics":
            show_revenue_analytics()
        elif page == "Product Performance":
            show_product_performance()
        elif page == "Customer Insights":
            show_customer_insights()
        elif page == "Experiment Results":
            show_experiment_results()

    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.info("Please ensure the database is running and the pipeline has been executed.")

def show_overview():
    st.header("📈 Key Performance Indicators")

    kpi_data = load_kpi_data()

    # KPI Cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Revenue",
            f"₹{kpi_data['total_revenue'].iloc[0]:,.0f}",
            help="Total revenue from all orders"
        )
        st.metric(
            "Total Orders",
            f"{kpi_data['total_orders'].iloc[0]:,}",
            help="Total number of orders placed"
        )

    with col2:
        st.metric(
            "Conversion Rate",
            f"{kpi_data['conversion_rate'].iloc[0]}%",
            help="Percentage of sessions that resulted in orders"
        )
        st.metric(
            "Average Order Value",
            f"₹{kpi_data['avg_order_value'].iloc[0]:,.0f}",
            help="Average value of each order"
        )

    with col3:
        st.metric(
            "Total Customers",
            f"{kpi_data['total_customers'].iloc[0]:,}",
            help="Total number of unique customers"
        )
        st.metric(
            "Total Sessions",
            f"{kpi_data['total_sessions'].iloc[0]:,}",
            help="Total number of website sessions"
        )

    st.markdown("---")

    # Recent Revenue Trend
    st.subheader("Revenue Trend (Last 30 Days)")
    revenue_data = load_revenue_trends()

    if not revenue_data.empty:
        # Filter last 30 days
        recent_data = revenue_data.tail(30)

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(recent_data['date'], recent_data['revenue'], marker='o', linewidth=2)
        ax.set_title('Daily Revenue Trend', fontsize=16, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Revenue (₹)', fontsize=12)
        ax.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x:,.0f}'))

        st.pyplot(fig)
    else:
        st.info("No revenue data available for the last 30 days.")

def show_revenue_analytics():
    st.header("💰 Revenue Analytics")

    revenue_data = load_revenue_trends()

    if revenue_data.empty:
        st.info("No revenue data available.")
        return

    # Monthly Revenue Chart
    st.subheader("Monthly Revenue")
    monthly_revenue = revenue_data.groupby(['year', 'month_name'])['revenue'].sum().reset_index()
    monthly_revenue['month_year'] = monthly_revenue['month_name'] + ' ' + monthly_revenue['year'].astype(str)

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(monthly_revenue['month_year'], monthly_revenue['revenue'])
    ax.set_title('Monthly Revenue', fontsize=16, fontweight='bold')
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Revenue (₹)', fontsize=12)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x:,.0f}'))
    plt.xticks(rotation=45)

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                f'₹{height:,.0f}', ha='center', va='bottom', fontsize=10)

    st.pyplot(fig)

    # Revenue vs Orders Scatter
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Revenue vs Orders")
        fig, ax = plt.subplots(figsize=(8, 6))
        scatter = ax.scatter(revenue_data['orders'], revenue_data['revenue'],
                           alpha=0.6, s=50, c=revenue_data['avg_order_value'], cmap='viridis')
        ax.set_xlabel('Number of Orders', fontsize=12)
        ax.set_ylabel('Revenue (₹)', fontsize=12)
        ax.set_title('Revenue vs Orders by Day', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x:,.0f}'))

        # Add colorbar
        cbar = plt.colorbar(scatter)
        cbar.set_label('Avg Order Value (₹)')

        st.pyplot(fig)

    with col2:
        st.subheader("Average Order Value Trend")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(revenue_data['date'], revenue_data['avg_order_value'], marker='o', color='orange')
        ax.set_title('Average Order Value Over Time', fontsize=14, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Average Order Value (₹)', fontsize=12)
        ax.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x:,.0f}'))

        st.pyplot(fig)

def show_product_performance():
    st.header("📦 Product Performance")

    product_data = load_product_performance()

    if product_data.empty:
        st.info("No product performance data available.")
        return

    # Top Products by Revenue
    st.subheader("Top 10 Products by Revenue")

    top_products = product_data.head(10)

    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(top_products['product_name'], top_products['revenue'])
    ax.set_title('Top 10 Products by Revenue', fontsize=16, fontweight='bold')
    ax.set_xlabel('Revenue (₹)', fontsize=12)
    ax.set_ylabel('Product Name', fontsize=12)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x:,.0f}'))

    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width + width*0.01, bar.get_y() + bar.get_height()/2,
                f'₹{width:,.0f}', ha='left', va='center', fontsize=10)

    st.pyplot(fig)

    # Category Performance
    st.subheader("Performance by Category")

    category_perf = product_data.groupby('category').agg({
        'revenue': 'sum',
        'units_sold': 'sum',
        'avg_price': 'mean'
    }).round(2).reset_index()

    col1, col2 = st.columns(2)

    with col1:
        # Revenue by Category
        fig, ax = plt.subplots(figsize=(8, 6))
        wedges, texts, autotexts = ax.pie(category_perf['revenue'],
                                        labels=category_perf['category'],
                                        autopct='%1.1f%%', startangle=90)
        ax.set_title('Revenue Share by Category', fontsize=14, fontweight='bold')
        plt.setp(autotexts, size=10, weight="bold")
        st.pyplot(fig)

    with col2:
        # Units Sold by Category
        fig, ax = plt.subplots(figsize=(8, 6))
        bars = ax.bar(category_perf['category'], category_perf['units_sold'])
        ax.set_title('Units Sold by Category', fontsize=14, fontweight='bold')
        ax.set_xlabel('Category', fontsize=12)
        ax.set_ylabel('Units Sold', fontsize=12)
        plt.xticks(rotation=45)

        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                    f'{height:,.0f}', ha='center', va='bottom', fontsize=10)

        st.pyplot(fig)

    # Product Performance Table
    st.subheader("Detailed Product Performance")
    st.dataframe(product_data.style.format({
        'revenue': '₹{:,.0f}',
        'avg_price': '₹{:,.0f}',
        'revenue_share': '{:.1f}%'
    }))

def show_customer_insights():
    st.header("👥 Customer Insights")

    customer_data = load_customer_segments()

    if customer_data.empty:
        st.info("No customer data available.")
        return

    # Customer Segment Overview
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Customers", f"{customer_data['customers'].sum():,}")

    with col2:
        st.metric("Total Revenue", f"₹{customer_data['revenue'].sum():,.0f}")

    with col3:
        st.metric("Avg Order Value", f"₹{customer_data['avg_order_value'].mean():,.0f}")

    # Customer Segments
    st.subheader("Customer Segments")

    col1, col2 = st.columns(2)

    with col1:
        # Revenue by Segment
        fig, ax = plt.subplots(figsize=(8, 6))
        wedges, texts, autotexts = ax.pie(customer_data['revenue'],
                                        labels=customer_data['customer_segment'],
                                        autopct='%1.1f%%', startangle=90)
        ax.set_title('Revenue Share by Customer Segment', fontsize=14, fontweight='bold')
        plt.setp(autotexts, size=10, weight="bold")
        st.pyplot(fig)

    with col2:
        # Orders by Segment
        fig, ax = plt.subplots(figsize=(8, 6))
        bars = ax.bar(customer_data['customer_segment'], customer_data['orders'])
        ax.set_title('Orders by Customer Segment', fontsize=14, fontweight='bold')
        ax.set_xlabel('Customer Segment', fontsize=12)
        plt.xticks(rotation=45)

        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                    f'{height:,.0f}', ha='center', va='bottom', fontsize=10)

        st.pyplot(fig)

    # Customer Segment Table
    st.subheader("Customer Segment Details")
    st.dataframe(customer_data.style.format({
        'customers': '{:,.0f}',
        'orders': '{:,.0f}',
        'revenue': '₹{:,.0f}',
        'avg_order_value': '₹{:,.0f}',
        'revenue_share': '{:.1f}%'
    }))

def show_experiment_results():
    st.header("🧪 A/B Test Results")

    experiment_data = load_experiment_results()

    if experiment_data.empty:
        st.info("No experiment data available.")
        return

    # Experiment Overview
    st.subheader("Experiment Performance")

    # Group by experiment
    experiments = experiment_data.groupby('experiment_name')

    for exp_name, exp_data in experiments:
        st.markdown(f"### {exp_name}")

        col1, col2, col3 = st.columns(3)

        # Calculate metrics for each variant
        for idx, row in exp_data.iterrows():
            with col1:
                st.metric(f"{row['variant']} Conversion", f"{row['conversion_rate']}%")
            with col2:
                st.metric(f"{row['variant']} Revenue", f"₹{row['revenue']:,.0f}")
            with col3:
                st.metric(f"{row['variant']} Orders", f"{row['orders']:,}")

        # Conversion Rate Comparison
        fig, ax = plt.subplots(figsize=(8, 4))
        bars = ax.bar(exp_data['variant'], exp_data['conversion_rate'])
        ax.set_title(f'{exp_name} - Conversion Rate by Variant', fontsize=14, fontweight='bold')
        ax.set_xlabel('Variant', fontsize=12)
        ax.set_ylabel('Conversion Rate (%)', fontsize=12)

        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height:.1f}%', ha='center', va='bottom', fontsize=10)

        st.pyplot(fig)

        st.markdown("---")

    # Detailed Experiment Table
    st.subheader("Detailed Experiment Results")
    st.dataframe(experiment_data.style.format({
        'sessions': '{:,.0f}',
        'orders': '{:,.0f}',
        'conversion_rate': '{:.1f}%',
        'revenue': '₹{:,.0f}',
        'avg_order_value': '₹{:,.0f}'
    }))

if __name__ == "__main__":
    main()