
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

```text
src/        → Data generation + ETL pipeline  
sql/        → Schema design + analytical queries  
notebooks/  → Business analysis (funnel, cohort, RFM, CLV)  
dashboard/  → Power BI dashboard  
data/       → Raw & processed data (ignored in Git)  
main.py     → Pipeline execution script  
```

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

