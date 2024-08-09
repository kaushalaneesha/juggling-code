-- customers (customer_id, first_name, last_name, city)
-- orders (order_id, customer_id, order_date, total_amount)

-- Identify customers who made at least 3 purchases within a one-month period and spent a total of more than $1000 during that period.

with mothly_orders AS (
    SELECT
    customer_id, 
    STRFTIME('%Y-%m', order_date) AS month
    SUM(total_amount) AS total_amount, 
    COUNT(order_id) AS total_orders
    FROM orders
    GROUP BY customer_id, year_month
)
SELECT 
    DISTINCT customer_id, 
    customer_name
FROM mothly_orders mo INNER JOIN customers c
ON mo.customer_id = c.customer_id
WHERE
    mo.total_orders > 3
    and mo.total_amount > 1000

