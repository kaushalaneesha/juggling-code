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