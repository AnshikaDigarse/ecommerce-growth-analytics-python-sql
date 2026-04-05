# 📊 Ecommerce Growth Platform (RetailFlow)

An end-to-end **product analytics and experimentation platform** designed to simulate how modern ecommerce companies track user behavior, optimize conversions, and drive revenue growth.

This project replicates a **real-world data analyst / product analytics workflow** — from raw data generation to insights, experimentation, and dashboarding.

---

## 🎯 Problem Statement

Ecommerce businesses struggle to answer critical questions:

* Where are users dropping off in the funnel?
* Which discounts actually drive revenue vs kill margins?
* Do experiments (A/B tests) truly impact conversions?
* Which customers bring long-term value?

This platform is built to **turn raw behavioral data into actionable business decisions**.

---

## 💡 What This Project Solves

* Tracks **user journey from session → cart → purchase**
* Measures **conversion funnel performance**
* Evaluates **pricing & discount strategies**
* Performs **A/B experimentation (statistical testing)**
* Analyzes **customer retention & lifetime value**
* Provides a **Power BI dashboard (RetailFlow)** for stakeholders

---

## 🏗️ Architecture Overview

```
Raw Data → Data Generation → Validation → Metrics → Analysis → Dashboard
```

### 🔹 Project Structure

```
ecommerce_growth_platform/
│
├── data/
│   ├── raw/                 # Synthetic event-level datasets
│   ├── processed/           # Cleaned & transformed data
│
├── src/
│   ├── core/                # Config & utilities
│   ├── data_generation/     # Data simulation scripts
│   ├── metrics/             # KPI computations
│   ├── pipeline/            # Validation & ETL logic
│
├── notebooks/               # Business analysis layer
│   ├── eda customer behaviour
│   ├── customer funnel
│   ├── A/B experimentation
│   ├── retention cohort
│   ├── pricing & margin
│   ├── CLTV segmentation
│
├── sql/
│   ├── schema.sql
│   ├── star_schema.sql
│   ├── analysis_queries.sql
│
├── dashboard/
│   ├── ecommerce_dashboard.pbix  # RetailFlow Dashboard
│
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
```

---

## 📊 Key Analyses & Business Impact

### 1️⃣ Exploratory Data Analysis (Customer Behavior)

Analyzed raw behavioral data to understand user patterns before applying advanced analytics.

**Key Focus Areas:**
- Session activity distribution  
- Product views and cart interactions  
- Purchase frequency and order value  
- Customer acquisition channels  
- Data quality and missing values  

👉 Key Insights:

- Majority of users drop off **before adding items to cart**, indicating weak product engagement  
- Significant drop observed at **cart → purchase stage**, suggesting checkout friction  
- Revenue distribution is **highly skewed**, with a small segment driving most revenue (Pareto effect)  
- Some acquisition channels bring traffic but **low conversion efficiency**  

👉 Business Impact:

> Established the foundation for funnel optimization, experimentation design, and customer segmentation strategy  

---

### 2️⃣ Conversion Funnel Analysis

Identified drop-offs across:
- Session → Cart  
- Cart → Purchase  

Helped detect friction points in checkout flow  

👉 Business Impact:

> Enables product teams to optimize UX and increase conversion rate  

---

### 3️⃣ A/B Experimentation (Pricing Strategy)

- Control Group: Low discount  
- Treatment Group: Higher discount  

**Statistical tests used:**
- Z-test (conversion rate)  
- T-test (revenue impact)  
- Chi-square (distribution differences)  

👉 Business Insight:

> Higher discounts increased conversions but reduced margin — highlighting trade-off between growth vs profitability  

---

### 4️⃣ Customer Retention & Cohort Analysis

- Monthly cohort tracking  
- Repeat purchase behavior  

👉 Business Insight:

> Early retention strongly correlates with long-term revenue  

---

### 5️⃣ Pricing & Margin Analysis

- Discount vs Revenue vs Margin relationship  

👉 Key Finding:

> Aggressive discounting increases revenue short-term but erodes profitability  

---

### 6️⃣ Customer Segmentation (CLTV)

Segmented users based on:
- Purchase frequency  
- Revenue contribution  

👉 Business Use:

> Enables targeted marketing and high-value customer retention  

---

## 📈 Dashboard – RetailFlow (Power BI)

The **RetailFlow dashboard** provides:

* Funnel conversion metrics
* Revenue & margin tracking
* Experiment performance
* Customer segmentation insights

👉 Designed for:

* Product Managers
* Business Teams
* Leadership decision-making

---

## ⚙️ Tech Stack

* **Python** (Pandas, NumPy)
* **SQL** (Data modeling, analytics queries)
* **Power BI** (Dashboarding)
* **Statistics** (Hypothesis testing, experimentation)
* **Data Modeling** (Star schema)

---

## 🔄 Data Pipeline

1. Synthetic data generation
2. Data validation & cleaning
3. Feature engineering
4. KPI computation
5. Analytical modeling
6. Dashboard visualization

---

## 🚀 How to Run

```bash
# Clone repository
git clone https://github.com/your-username/ecommerce-growth-platform.git

# Install dependencies
pip install -r requirements.txt

# Run data generation
python src/data_generation/generate_orders.py

# Run validation pipeline
python src/pipeline/data_validation.py
```

---

## 🎯 Key Skills Demonstrated

* Product Analytics Thinking
* A/B Testing & Hypothesis Testing
* SQL Data Modeling (Star Schema)
* End-to-End Data Pipeline Design
* Dashboard Storytelling (Power BI)
* Business Decision Making with Data

---

## 🧠 What Makes This Project Stand Out

This is not just a dashboard or notebook collection.

It simulates how **real companies operate data teams**:

* Data Engineers → pipelines
* Analysts → insights
* Product → decisions

---

## 📌 Future Improvements

* Real-time data pipeline (Kafka / streaming)
* ML-based recommendation system
* Automated experiment tracking system

---

## 👤 Author

Anshika Digarse –  Data Analyst
Focused on building **real-world, decision-driven data systems**

---

## ⭐ If you found this useful

Give this repo a star ⭐ — it helps visibility and reach!
