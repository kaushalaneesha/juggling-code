-- Table: students

-- id	name	score
-- 1	John	85
-- 2	Alice	90
-- 3	Bob	85
-- 4	Carol	95
-- 5	Dave	90
-- Question: Write a query to rank the students by their scores. If two students have the same score, they should have the same rank, and the next rank should skip the appropriate number of positions (i.e., use the RANK() function).

SELECT 
    id, 
    name, 
    score
    RANK() OVER(order by score desc) AS `rank`
FROM students
;

-- Question 2: Calculate Running Total of Sales
-- Table: sales

-- sale_id	sale_date	amount
-- 1	2024-01-01	100
-- 2	2024-01-02	200
-- 3	2024-01-03	150
-- 4	2024-01-04	250
-- 5	2024-01-05	300
-- Question: Write a query to calculate the running total of sales amount, ordered by the sale date.


SELECT 
    sale_id,
    sale_date, 
    SUM(amount) OVER(order by sale_date) AS sale_total 
FROM 
    sales
ORDER BY 
    date
;

-- Question 3: Find Employees with Salaries Above Average in Their Department
-- Table: employees

-- emp_id	emp_name	department	salary
-- 1	John	HR	60000
-- 2	Alice	HR	65000
-- 3	Bob	IT	70000
-- 4	Carol	IT	80000
-- 5	Dave	IT	75000
-- Question: Write a query to find employees who have a salary above the average salary of their department.

WITH avg_salary AS (
    SELECT 
        department,
        AVG(salary) AS asalary
    FROM 
        Employees
    GROUP BY 
        department
)
SELECT 
    e.emp_id,
    e.emp_name, 
    e.department,
    e.salary
FROM 
    employees e
    INNER JOIN avg_salary a
    ON e.department = a.department
WHERE   
    e.salary > a.asalary
;

-- Question 4: Find Top 3 Salaries in Each Department
-- Table: employees

-- emp_id	emp_name	department	salary
-- 1	John	HR	60000
-- 2	Alice	HR	65000
-- 3	Bob	IT	70000
-- 4	Carol	IT	80000
-- 5	Dave	IT	75000
-- 6	Eve	HR	62000
-- 7	Frank	IT	78000
-- Question: Write a query to find the top 3 highest salaries in each department.

WITH RankedEmployees AS (
    SELECT 
        emp_id, 
        emp_name,
        department,
        salary, 
        DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS rank
    FROM 
        employee
)
SELECT 
    emp_id, 
    emp_name,
    department,
    salary, 
    rank
FROM 
    RankedEmployees
WHERE
    rank <= 3;