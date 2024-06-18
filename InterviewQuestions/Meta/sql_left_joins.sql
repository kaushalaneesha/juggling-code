-- Description:
-- You have two tables, Orders and Customers. The Orders table contains information about orders placed, and the Customers table contains information about the customers who placed these orders. Some orders might not have associated customer information.

-- Orders table:

-- order_id (int)
-- customer_id (int)
-- order_date (date)
-- total_amount (decimal)
-- Customers table:

-- customer_id (int)
-- customer_name (varchar)
-- customer_email (varchar)
-- Question:
-- Write an SQL query to retrieve all orders along with the customer name and email. If an order does not have a corresponding customer, return NULL for the customer name and email.


SELECT 
    o.order_id, 
    o.order_date, 
    o.total_amount, 
    c.customer_name, 
    c.customer_email
FROM 
    orders o
    LEFT JOIN customers c
    ON o.customer_id = c.customer_id
;