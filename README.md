
# 📊 E-commerce Growth Analytics Platform

A full-stack data analytics project that simulates an e-commerce environment to analyze customer behavior, improve conversion, and drive business growth using **Python, SQL, and Power BI**.

---

# 🎯 Business Objective

This project is designed to answer key business questions:

* Where are users dropping in the purchase funnel?
* Are customers returning after their first purchase?
* Which customers drive the most revenue?
* How do product features impact user behavior?

---

# 🏗️ End-to-End Architecture

```text
Data Generation (Python)
↓
Raw Data (CSV)
↓
ETL Pipeline (Python)
↓
Data Warehouse (SQL Star Schema)
↓
Analytics Layer (Notebooks)
↓
Dashboard (Power BI)
```

---

# 🧱 Project Structure

This project follows a modular and scalable architecture separating data generation, processing, analytics, and visualization layers.

---

## 📁 Root Directory

ecommerce_growth_platform/
│
├── src/                     # Core source code  
├── sql/                     # Database schema & queries  
├── notebooks/              # Analysis notebooks  
├── dashboard/              # Power BI dashboard  
├── data/                   # Raw & processed data (ignored in Git)  
├── docs/                   # Documentation  
│
├── main.py                 # Pipeline entry point  
├── README.md               # Project overview  
├── requirements.txt        # Dependencies  
├── .env.example            # Environment template  
├── .gitignore              # Ignore rules  

---

## 🔹 src/ (Core Logic)

src/
│
├── core/
│   ├── config.py           # Config & DB connection  
│   ├── utils.py            # Helper functions  
│
├── data_generation/
│   ├── generate_customers.py  
│   ├── generate_products.py  
│   ├── generate_sessions.py  
│   ├── generate_cart_events.py  
│   ├── generate_orders.py  
│
├── pipeline/
│   ├── etl_pipeline.py     # ETL logic  
│   ├── data_validation.py  # Data quality checks  
│
├── metrics/
│   ├── business_metrics.py # KPI calculations  

---

## 🔹 sql/ (Database Layer)

sql/
│
├── schema.sql              # Base tables  
├── star_schema.sql         # Fact & dimension tables  
├── analytics_queries.sql   # Business queries  

---

## 🔹 notebooks/ (Analysis)

notebooks/
│
├── 01_eda_customer_behavior.ipynb  
├── 02_conversion_funnel_analysis.ipynb  
├── 03_ab_experimentation.ipynb  
├── 04_customer_retention_cohort.ipynb  
├── 05_pricing_margin_analysis.ipynb  
├── 06_customer_segmentation_rfm.ipynb  

---

## 🔹 dashboard/ (Visualization)

dashboard/
│
├── ecommerce_dashboard.pbix  
├── RetailFlow.json  

---

## 🔹 data/ (Storage)

data/
│
├── raw/        # Generated data  
├── processed/  # Cleaned data  

(Note: This folder is ignored in Git)

---

## 🔹 docs/ (Documentation)

docs/
│
├── architecture.md  
├── data_dictionary.md  

---

## 🔁 Pipeline Flow

Data Generation → Raw Data → Validation → ETL → Processed Data → MySQL → Star Schema → Analytics → Dashboard

---

## 📌 Key Design Principles

- Modular structure  
- Separation of concerns  
- Reusable components  
- Business-focused analytics  
- Clean and maintainable code  

---

---

# 📊 Key Analyses

### 🔹 Funnel Analysis

* Identifies drop-offs across user journey
* Helps improve conversion rate

### 🔹 Cohort & Retention Analysis

* Tracks user retention over time
* Measures repeat customer behavior

### 🔹 A/B Testing

* Evaluates impact of product changes
* Measures conversion uplift

### 🔹 Customer Segmentation (RFM)

* Identifies high-value customers
* Segments users into Champions, Loyal, At Risk

### 🔹 Customer Lifetime Value (CLV)

* Measures long-term customer value
* Helps prioritize high-value segments

### 🔹 Feature Adoption Analysis

* Tracks user engagement
* Identifies behavior driving revenue

---

# 📊 Key Business Metrics

* Conversion Rate
* Cart Abandonment Rate
* Retention Rate
* Average Order Value (AOV)
* Customer Lifetime Value (CLV)

---

# 📈 Dashboard

Interactive Power BI dashboard showcasing:

* Funnel drop-offs
* Retention trends
* Customer segments
* Revenue insights

![Dashboard](dashboard/screenshot.png)

---

# 🛠️ Tech Stack

* Python (Pandas, NumPy)
* SQL (MySQL / PostgreSQL)
* Power BI
* Git & GitHub

---

# 🚀 Key Highlights

* Built an end-to-end analytics pipeline from data generation to dashboarding
* Implemented real-world product analytics techniques
* Designed a scalable and modular data system
* Focused on business-driven insights, not just data processing

---

# 🔮 Future Improvements

* Real-time data pipeline
* Recommendation system
* Advanced experimentation framework

