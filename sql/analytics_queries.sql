USE ecommerce_analytics;

-- Conversion Rate
SELECT
COUNT(DISTINCT o.session_id) * 1.0 /
COUNT(DISTINCT s.session_id) AS conversion_rate
FROM fact_sessions s
LEFT JOIN fact_orders o
ON s.session_id = o.session_id;


-- Revenue by Experiment Group
SELECT
c.ab_group,
SUM(o.final_price) AS revenue
FROM fact_orders o
JOIN dim_customer c
ON o.customer_id = c.customer_id
GROUP BY c.ab_group;


-- Margin by Experiment Group
SELECT
c.ab_group,
SUM(o.margin) AS total_margin
FROM fact_orders o
JOIN dim_customer c
ON o.customer_id = c.customer_id
GROUP BY c.ab_group;


-- Customer Lifetime Value
SELECT
c.ab_group,
AVG(customer_revenue) AS avg_ltv
FROM (

SELECT
o.customer_id,
c.ab_group,
SUM(o.final_price) AS customer_revenue
FROM fact_orders o
JOIN dim_customer c
ON o.customer_id = c.customer_id
GROUP BY o.customer_id, c.ab_group

) t
GROUP BY ab_group;