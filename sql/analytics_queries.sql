USE ecommerce_analytics;

-- =====================================================
-- 1️⃣ FUNNEL ANALYSIS
-- =====================================================

-- Step counts
SELECT
    COUNT(DISTINCT s.session_id) AS total_sessions,
    COUNT(DISTINCT c.session_id) AS cart_sessions,
    COUNT(DISTINCT o.session_id) AS purchase_sessions
FROM fact_sessions s
LEFT JOIN fact_cart_events c ON s.session_id = c.session_id
LEFT JOIN fact_orders o ON s.session_id = o.session_id;


-- Funnel Conversion Rates
SELECT
    COUNT(DISTINCT o.session_id) * 1.0 / COUNT(DISTINCT s.session_id) AS overall_conversion_rate,
    COUNT(DISTINCT o.session_id) * 1.0 / COUNT(DISTINCT c.session_id) AS cart_to_purchase_rate
FROM fact_sessions s
LEFT JOIN fact_cart_events c ON s.session_id = c.session_id
LEFT JOIN fact_orders o ON s.session_id = o.session_id;


-- Funnel by Device
SELECT
    s.device,
    COUNT(DISTINCT s.session_id) AS sessions,
    COUNT(DISTINCT o.session_id) AS purchases,
    COUNT(DISTINCT o.session_id) * 1.0 / COUNT(DISTINCT s.session_id) AS conversion_rate
FROM fact_sessions s
LEFT JOIN fact_orders o ON s.session_id = o.session_id
GROUP BY s.device;


-- =====================================================
-- 2️⃣ REVENUE & MARGIN ANALYSIS
-- =====================================================

SELECT
    ab_group,
    SUM(final_price) AS total_revenue,
    SUM(margin) AS total_margin
FROM fact_orders
GROUP BY ab_group;


-- Average Order Value
SELECT
    ab_group,
    AVG(final_price) AS avg_order_value
FROM fact_orders
GROUP BY ab_group;


-- =====================================================
-- 3️⃣ RFM SEGMENTATION (IMPORTANT 🔥)
-- =====================================================

WITH rfm_base AS (
    SELECT
        customer_id,
        MAX(order_date) AS last_order_date,
        COUNT(order_id) AS frequency,
        SUM(final_price) AS monetary
    FROM fact_orders
    GROUP BY customer_id
),

rfm_calc AS (
    SELECT
        customer_id,
        DATEDIFF(MAX(order_date), last_order_date) AS recency,
        frequency,
        monetary
    FROM rfm_base
    JOIN fact_orders USING (customer_id)
    GROUP BY customer_id, last_order_date, frequency, monetary
)

SELECT *
FROM rfm_calc;


-- =====================================================
-- 4️⃣ CUSTOMER LIFETIME VALUE (CLV)
-- =====================================================

SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    SUM(final_price) AS total_revenue,
    AVG(final_price) AS AOV,
    SUM(final_price) AS CLV
FROM fact_orders
GROUP BY customer_id;


-- CLV by segment
SELECT
    ab_group,
    AVG(customer_revenue) AS avg_clv
FROM (
    SELECT
        customer_id,
        ab_group,
        SUM(final_price) AS customer_revenue
    FROM fact_orders
    GROUP BY customer_id, ab_group
) t
GROUP BY ab_group;


-- =====================================================
-- 5️⃣ COHORT ANALYSIS (RETENTION)
-- =====================================================

WITH first_purchase AS (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM fact_orders
    GROUP BY customer_id
),

cohort_data AS (
    SELECT
        o.customer_id,
        DATE_FORMAT(f.first_order_date, '%Y-%m') AS cohort_month,
        TIMESTAMPDIFF(
            MONTH,
            f.first_order_date,
            o.order_date
        ) AS months_since
    FROM fact_orders o
    JOIN first_purchase f
    ON o.customer_id = f.customer_id
)

SELECT
    cohort_month,
    months_since,
    COUNT(DISTINCT customer_id) AS active_users
FROM cohort_data
GROUP BY cohort_month, months_since
ORDER BY cohort_month, months_since;


-- =====================================================
-- 6️⃣ TOP CUSTOMERS
-- =====================================================

SELECT
    customer_id,
    SUM(final_price) AS total_revenue
FROM fact_orders
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 10;