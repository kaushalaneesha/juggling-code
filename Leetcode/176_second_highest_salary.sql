# Write your MySQL query statement below
WITH ranked_salary AS(
SELECT 
    salary, 
    DENSE_RANK() OVER(ORDER BY salary desc) AS d_rank
FROM 
    Employee
)
SELECT 
    IFNULL(
        (SELECT 
            DISTINCT(salary) 
        FROM 
            ranked_salary 
        WHERE d_rank = 2), NULL) AS SecondHighestSalary;
