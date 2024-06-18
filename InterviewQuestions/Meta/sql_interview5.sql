
-- Sure, let's define the structure of the tables involved in the SQL query. We'll create three tables: PROD_CLASS, PROD, and SALES.

-- Table Structures
-- PROD_CLASS Table:
-- This table contains information about different product classes.

-- Column Name	Data Type	Description
-- prod_class_id	INT	Unique ID for the product class
-- class_name	VARCHAR	Name of the product class

-- PROD Table:
-- This table contains information about products. Each product belongs to a product class.
-- Column Name	Data Type	Description
-- prod_id	INT	Unique ID for the product
-- prod_class_id	INT	ID of the product class
-- prod_name	VARCHAR	Name of the product

-- SALES Table:
-- This table contains information about sales transactions.
-- Column Name	Data Type	Description
-- sale_id	INT	Unique ID for the sale transaction
-- prod_id	INT	ID of the product
-- unit_sold	INT	Number of units sold
-- promotion_id	INT	ID of the promotion applied (0 if no promotion)


-- Questions
-- Find the sum of units sold for each product class.
-- Calculate the ratio of units sold with a valid promotion to units sold without a valid promotion.
-- Order the results in increasing order of the total units sold.

SELECT 
    pc.class_name, 
    SUM(s.unit_sold) AS total_cost,
    CAST (SUM(CASE WHEN promotion_id > 0 THEN s.unit_sold ELSE 0 END) AS DECIMAL) / 
    SUM(CASE WHEN promotion_id = 0 THEN s.unit_sold ELSE 0 END)   AS    valid_ratio
FROM
    product_class pc
    INNER JOIN prod p ON pc.prod_class_id = p.prod_class_id
    INNER JOIN sales s ON p.prod_id = s.prod_id
GROUP BY 
    pc.class_name
ORDER BY 
    total_cost
;




SELECT 
    v.view_date,
    AVG(v.view_count) OVER(ORDER BY v.view_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) '3_day_running_average'
FROM 
    users u
    INNER JOIN view v
    ON u.user_id = v.user_id 
    and u.user_type = 'user'
;