USE ecommerce_analytics;

-- Disable foreign key checks to allow dropping tables with constraints
SET FOREIGN_KEY_CHECKS = 0;

-- Drop fact tables first (they have foreign keys)
DROP TABLE IF EXISTS fact_cart_events;
DROP TABLE IF EXISTS fact_orders;
DROP TABLE IF EXISTS fact_sessions;

-- Then drop dimension tables
DROP TABLE IF EXISTS dim_product;
DROP TABLE IF EXISTS dim_customer;

-- Re-enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;


CREATE TABLE dim_customer AS
SELECT
customer_id,
acquisition_channel,
ab_group
FROM customers;

ALTER TABLE dim_customer
ADD PRIMARY KEY (customer_id);


CREATE TABLE dim_product AS
SELECT
product_id,
category,
base_price,
cost
FROM products;

ALTER TABLE dim_product
ADD PRIMARY KEY (product_id);


CREATE TABLE fact_sessions AS
SELECT
session_id,
customer_id,
session_date,
device_type,
traffic_source,
pages_viewed,
session_duration,
bounced_flag
FROM sessions;

ALTER TABLE fact_sessions
ADD CONSTRAINT fk_sessions_customer
FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id);


CREATE TABLE fact_orders AS
SELECT
order_id,
session_id,
customer_id,
product_id,
quantity,
final_price,
margin,
discount_pct
FROM orders;

ALTER TABLE fact_orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
ADD CONSTRAINT fk_orders_product
FOREIGN KEY (product_id) REFERENCES dim_product(product_id);


CREATE TABLE fact_cart_events AS
SELECT *
FROM cart_events;

ALTER TABLE fact_cart_events
ADD CONSTRAINT fk_cart_customer
FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
ADD CONSTRAINT fk_cart_product
FOREIGN KEY (product_id) REFERENCES dim_product(product_id);