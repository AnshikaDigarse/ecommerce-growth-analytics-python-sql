CREATE DATABASE IF NOT EXISTS ecommerce_analytics;

USE ecommerce_analytics;

DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS cart_events;
DROP TABLE IF EXISTS orders;


CREATE TABLE customers (
    customer_id INT,
    acquisition_channel VARCHAR(50),
    ab_group VARCHAR(20)
);


CREATE TABLE products (
    product_id INT,
    category VARCHAR(50),
    base_price FLOAT,
    cost FLOAT
);


CREATE TABLE sessions (
    session_id INT,
    customer_id INT,
    session_date DATE,
    device_type VARCHAR(20),
    traffic_source VARCHAR(50),
    pages_viewed INT,
    session_duration INT,
    bounced_flag INT
);


CREATE TABLE cart_events (
    cart_event_id INT,
    session_id INT,
    customer_id INT,
    product_id INT,
    event_type VARCHAR(50),
    event_timestamp DATETIME
);


CREATE TABLE orders (
    order_id INT,
    session_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    final_price FLOAT,
    margin FLOAT,
    discount_pct FLOAT
);