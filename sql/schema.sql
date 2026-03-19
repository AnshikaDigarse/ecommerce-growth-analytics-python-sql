-- schema.sql

CREATE DATABASE IF NOT EXISTS ecommerce_analytics;
USE ecommerce_analytics;

DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS cart_events;
DROP TABLE IF EXISTS orders;

-- -----------------------
-- CUSTOMERS
-- -----------------------
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    acquisition_channel VARCHAR(50),
    ab_group VARCHAR(20)
);

-- -----------------------
-- PRODUCTS
-- -----------------------
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    category VARCHAR(50),
    base_price FLOAT,
    cost FLOAT,
    margin_pct FLOAT
);

-- -----------------------
-- SESSIONS
-- -----------------------
CREATE TABLE sessions (
    session_id INT PRIMARY KEY,
    customer_id INT,
    session_date DATE,
    device VARCHAR(20),
    traffic_source VARCHAR(50),
    pages_viewed INT,
    session_duration INT,
    bounced_flag INT
);

-- -----------------------
-- CART EVENTS
-- -----------------------
CREATE TABLE cart_events (
    cart_id INT PRIMARY KEY,
    session_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    event_type VARCHAR(50),
    event_timestamp DATETIME
);

-- -----------------------
-- ORDERS (UPDATED)
-- -----------------------
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    session_id INT,
    product_id INT,
    quantity INT,
    acquisition_channel VARCHAR(50),
    ab_group VARCHAR(20),
    original_price FLOAT,
    discount_amount FLOAT,
    final_price FLOAT,
    cost FLOAT,
    margin FLOAT,
    order_date DATETIME
);