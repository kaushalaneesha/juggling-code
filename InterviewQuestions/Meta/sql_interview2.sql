-- SQL questions: https://leetcode.com/discuss/interview-question/2071096/Meta-or-Dublin-or-Data-Engineer-(Reject)

-- find second highest salary:
SELECT 
    MAX(salary)
FROM 
    employee
WHERE salary != (SELECT max(salary) from employee)
GROUP BY salary

-- Using row number 
SELECT 
    salary 
  , DENSE_RANK OVER (order by salary desc) 
FROM 
    employee
WHERE
    row_number = 2
;

-- Find customers making maximum purchases

with customer_purchases AS
(SELECT 
    customer_id
  , count(*) AS purchases
FROM 
    sales
);

SELECT customer_id from customer_purchases where purchase = (select max(purchase) from customer_purchases);