-- Assuming tables
-- Salesperson: Id, Name, Age, Salary
-- Customer: Id, Name, City, Industry Type
-- Orders: Number, order_date, cust_id, salesperson_id, amount

-- a. The names of all salespeople that have an order with Samsonic.
SELECT 
    DISTINCT sp.name
FROM 
    salesperson sp
    INNER JOIN orders o ON sp.id = o.salesperson_id
    INNER JOIN customer c ON o.cust_id = c.id
WHERE 
    c.name = "Samsonic"

-- b. The names of all salespeople that do not have any order with Samsonic.
SELECT 
    sp.name
FROM 
    salesperson sp
    LEFT JOIN orders o ON sp.id = o.salesperson_id
    LEFT JOIN customer c ON o.cust_id = c.id
    AND c.name = 'Samsonic'
WHERE 
    c.id is NULL

-- c. The names of salespeople that have 2 or more orders.SELECT 
SELECT 
    sp.name
  , count(*) orders
FROM 
    salesperson sp
    INNER JOIN orders o
    ON sp.id = orders.salesperson_id
GROUP BY 
    sp.name
HAVING orders >= 2

-- d. The names and ages of all salespersons must having a salary of 100,000 or greater.
select
    name 
  , age
FROM 
    salesperson sp
WHERE 
    salary >= 100000
    
-- e. What sales people have sold more than 1400 total units?
SELECT 
    sp.name
  , SUM(amount) AS units
FROM 
    salesperson sp
    INNER JOIN orders o
    ON sp.id = orders.salesperson_id
GROUP BY 
    sp.name
HAVING units >= 1400

-- f. When was the earliest and latest order made to Samony?
WITH RANKED_ORDERS AS (
SELECT 
    o.number
  , order_date
  , amount
  , salesperson_id
  , DENSE_RANK() OVER(PARTITION BY cust_id ORDER BY order_date desc) latest_ordering
  , DENSE_RANK() OVER(PARTITION BY cust_id ORDER BY order_date asc) earliest_ordering
FROM 
    orders o
    INNER JOIN customer c
    ON orders.cust_id = customer.id
WHERE 
    c.name = "Samony"
)

SELECT * FROM RANKED_ORDERS WHERE latest_ordering = 1 OR earliest_ordering = 1

-- find the sales people with average sale greater then 3 atleast selling two products.
SELECT 
    sp.name 
  , COUNT(DISTINCT (product_id))     AS unique_products
  , COUNT(*)                         AS orders 
FROM 
    salesperson sp
    INNER JOIN orders o
    ON sp.id = o.salesperson_id
GROUP BY 
    sp.name
HAVING 
    AVG(orders) > 3
    and unique_products > 2

--what is the total percentage of sale of a product compared to sales.
SELECT 
    p.product_id,
    SUM(o.amount) AS product_sales,
    SUM(o.amount) / (SELECT SUM(amount) FROM orders) * 100 AS percentage_of_total_sales
FROM 
    orders o
GROUP BY 
    p.product_id
ORDER BY 
    product_sales 
DESC;
