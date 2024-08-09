-- Suppose we have 2 tables called Orders and Salesperson shown below:

-- Salesperson	Orders
-- ID	Name	Age	Salary
-- 1	Abe	61	140000
-- 2	Bob	34	44000
-- 5	Chris	34	40000
-- 7	Dan	41	52000
-- 8	Ken	57	115000
-- 11	Joe	38	38000
-- Number	order_date	cust_id	salesperson_id	Amount
-- 10	8/2/96	4	2	540
-- 20	1/30/99	4	8	1800
-- 30	7/14/95	9	1	460
-- 40	1/29/98	7	2	2400
-- 50	2/3/98	6	7	600
-- 60	3/2/98	6	7	720
-- 70	5/6/98	9	7	150

-- Now suppose that we want to write SQL that must conform to the SQL standard.


-- We want to retrieve the names of all salespeople that have more than 1 order from the tables above. You can assume that each salesperson only has one ID.
SELECT 
    s.name, 
    COUNT(*) order_count
FROM 
    salesperson s
    INNER JOIN orders o
    ON s.id = o.salesperson_id
GROUP BY 
    s.name
HAVING 
    COUNT(s.salesperson_id) > 1
;

