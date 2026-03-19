USE ecommerce_analytics;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS fact_cart_events;
DROP TABLE IF EXISTS fact_orders;
DROP TABLE IF EXISTS fact_sessions;
DROP TABLE IF EXISTS dim_product;
DROP TABLE IF EXISTS dim_customer;

SET FOREIGN_KEY_CHECKS = 1;

-- -----------------------
-- DIMENSIONS
-- -----------------------

CREATE TABLE dim_customer AS
SELECT
    customer_id,
    acquisition_channel,
    ab_group
FROM customers;

ALTER TABLE dim_customer ADD PRIMARY KEY (customer_id);


CREATE TABLE dim_product AS
SELECT
    product_id,
    category,
    base_price,
    cost,
    margin_pct
FROM products;

ALTER TABLE dim_product ADD PRIMARY KEY (product_id);

-- -----------------------
-- FACT TABLES
-- -----------------------

CREATE TABLE fact_sessions AS
SELECT
    session_id,
    customer_id,
    session_date,
    device,
    traffic_source,
    pages_viewed,
    session_duration,
    bounced_flag
FROM sessions;

ALTER TABLE fact_sessions
ADD FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id);


CREATE TABLE fact_orders AS
SELECT
    order_id,
    customer_id,
    session_id,
    product_id,
    quantity,
    acquisition_channel,
    ab_group,
    original_price,
    discount_amount,
    final_price,
    cost,
    margin,
    order_date
FROM orders;

ALTER TABLE fact_orders
ADD FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
ADD FOREIGN KEY (product_id) REFERENCES dim_product(product_id);


CREATE TABLE fact_cart_events AS
SELECT
    cart_id,
    session_id,
    customer_id,
    product_id,
    quantity,
    event_type,
    event_timestamp
FROM cart_events;

ALTER TABLE fact_cart_events
ADD FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
ADD FOREIGN KEY (product_id) REFERENCES dim_product(product_id);