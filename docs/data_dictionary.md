# 📊 Data Dictionary

---

## 🟢 Customers Table

- `customer_id`: Unique identifier for each customer  
- `acquisition_channel`: Source of customer (Organic, Paid Ads, Referral, Influencer)  
- `ab_group`: Experiment group (Control or Treatment)  

---

## 🟢 Products Table

- `product_id`: Unique product identifier  
- `category`: Product category (Electronics, Fashion, Home, Beauty, Grocery)  
- `base_price`: Base selling price  
- `cost`: Cost of product  
- `margin_pct`: Margin percentage  

---

## 🟢 Sessions Table

- `session_id`: Unique session identifier  
- `customer_id`: Customer who initiated the session  
- `session_date`: Date of session  
- `device`: Device used (Mobile, Desktop, Tablet)  
- `traffic_source`: Source of traffic  
- `pages_viewed`: Number of pages viewed  
- `session_duration`: Duration in seconds  
- `bounced_flag`: 1 = bounced, 0 = not bounced  

---

## 🟢 Cart Events Table

- `cart_id`: Unique cart event identifier  
- `session_id`: Associated session  
- `customer_id`: Customer identifier  
- `product_id`: Product added to cart  
- `quantity`: Quantity added  
- `event_type`: Event type (add_to_cart)  
- `event_timestamp`: Timestamp of event  

---

## 🔥 Orders Table

- `order_id`: Unique order identifier  
- `customer_id`: Customer placing the order  
- `session_id`: Session linked to purchase  
- `product_id`: Product purchased  
- `quantity`: Quantity purchased  
- `acquisition_channel`: Customer acquisition source  
- `ab_group`: Experiment group  
- `original_price`: Price before discount  
- `discount_amount`: Discount applied  
- `final_price`: Price after discount  
- `cost`: Cost of product  
- `margin`: Profit (final_price - cost)  
- `order_date`: Timestamp of purchase  

---

# 🏗️ Star Schema Tables

## Dimensions

- `dim_customer`: Customer attributes  
- `dim_product`: Product attributes  
- `dim_date`: Date-related attributes  

---

## Facts

- `fact_sessions`: Session-level activity  
- `fact_orders`: Transaction-level data  
- `fact_cart_events`: Cart interaction events  

---

# 📈 Derived Analytics Tables

---

## 🟣 RFM Segmentation

- `customer_id`: Unique customer identifier  
- `Recency`: Days since last purchase  
- `Frequency`: Total number of orders  
- `Monetary`: Total revenue spent  
- `R_score`: Recency score (1-5, 5 = most recent)  
- `F_score`: Frequency score (1-5, 5 = most frequent)  
- `M_score`: Monetary score (1-5, 5 = highest spending)  
- `RFM_Score`: Combined RFM score (e.g., "555")  
- `Segment`: Customer segment (Champions, Loyal, At Risk, Lost)  

---

## 🟣 Customer Lifetime Value (CLV)

- `customer_id`: Unique customer identifier  
- `total_orders`: Total number of orders  
- `total_revenue`: Total revenue generated  
- `AOV`: Average Order Value  
- `CLV`: Customer Lifetime Value  

---