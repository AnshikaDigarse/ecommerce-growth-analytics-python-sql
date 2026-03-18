# Architecture Diagram

[Customer Simulation Engine]
        ↓
[Session & Cart Engine]
        ↓
[Order Engine]
        ↓
--------------------------
      Raw Data (CSV)
--------------------------
        ↓
      ETL Pipeline
        ↓
--------------------------
     Data Warehouse
 (Star Schema - SQL)
--------------------------
        ↓
   Analytics Notebooks
        ↓
   Business Insights
        ↓
   Power BI Dashboard