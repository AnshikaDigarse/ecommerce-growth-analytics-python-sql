# Data Dictionary

## Customers Table
- `customer_id`: Unique identifier for each customer
- `acquisition_channel`: How the customer was acquired (Organic, Paid Ads, Referral, Influencer)
- `ab_group`: Experiment group (Control or Treatment)

## Sessions Table
- `session_id`: Unique session identifier
- `customer_id`: Customer who started the session
- `session_date`: Date of the session
- `device_type`: Device used (Mobile, Desktop)
- `traffic_source`: Traffic source
- `pages_viewed`: Number of pages viewed
- `session_duration`: Session duration in seconds
- `bounced_flag`: Whether the session bounced (1=yes, 0=no)

## Cart Events Table
- `session_id`: Session identifier
- `customer_id`: Customer identifier
- `product_id`: Product added to cart
- `event_type`: Type of cart event

## Orders Table
- `order_id`: Unique order identifier
- `customer_id`: Customer who placed the order
- `session_id`: Session during which order was placed
- `product_id`: Product ordered
- `quantity`: Quantity ordered
- `ab_group`: Experiment group
- `acquisition_channel`: Customer acquisition channel
- `original_price`: Original product price
- `discount_pct`: Discount percentage applied
- `discount_amount`: Discount amount
- `final_price`: Final price paid
- `cost`: Product cost
- `margin`: Profit margin

## Products Table
- `product_id`: Unique product identifier
- `category`: Product category (Electronics, Fashion, Home, Beauty, Grocery)
- `base_price`: Base selling price in ₹
- `margin_pct`: Margin percentage
- `cost`: Cost price in ₹

## Star Schema Tables

### Dimensions
- `dim_customer`: Customer attributes
- `dim_product`: Product attributes
- `dim_date`: Date dimension

### Facts
- `fact_sessions`: Session-level metrics
- `fact_orders`: Order-level transactions
- `fact_cart_events`: Cart interaction events

## Derived Analytics Tables

### RFM Segmentation Table
- `customer_id`: Unique customer identifier
- `Recency`: Days since last purchase
- `Frequency`: Total number of orders
- `Monetary`: Total revenue spent
- `R_score`: Recency score (1-5, 5=most recent)
- `F_score`: Frequency score (1-5, 5=most frequent)
- `M_score`: Monetary score (1-5, 5=highest spending)
- `RFM_Score`: Combined RFM score string (e.g., "555")
- `Segment`: Customer segment (Champions, Loyal, Potential Loyalist, At Risk, Lost)

### Customer Lifetime Value Table
- `customer_id`: Unique customer identifier
- `total_orders`: Total number of orders placed
- `total_revenue`: Total revenue generated
- `AOV`: Average Order Value (total_revenue / total_orders)
- `CLV`: Customer Lifetime Value (AOV * total_orders)