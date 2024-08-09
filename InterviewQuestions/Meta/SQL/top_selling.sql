-- Problem: Find the top 5 best-selling products by revenue in the past year, categorized by product category.

-- Table Structure:

-- Products: product_id (PK), product_name, category_id
-- Orders: order_id (PK), customer_id, order_date
-- Order_Items: order_item_id (PK), order_id, product_id, quantity, unit_price

CREATE INDEX idx_order_items_product_id ON Order_Items (product_id);
CREATE INDEX idx_orders_order_date ON Orders (order_date);

WITH product_revenue AS (
    SELECT 
        product_id,
        SUM(unit_price) * quantity AS revenue
    FROM 
        order_items oi
        INNER JOIN Orders o
        ON or.order_id = o.order_id
    WHERE  
        order_date >= DATE_ADD(CURDATE(), INTERVAL -1 YEAR)
    GROUP BY 
        product_id
), ranked_products AS (
SELECT 
    category_id, 
    product_id,
    product_name, 
    DENSE_RANK() OVER (PARTITION BY category_id ORDER BY  revenue desc) AS rnk
FROM 
    products p
    INNER JOIN product_revenue pr
    ON p.product_id = pr.product_id
)
SELECT category_id, product_name from ranked_products where rnk <= 5;


