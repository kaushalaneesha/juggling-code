-- Author: id, name, last_name, nationality
-- Books: Book_id, title, author_id, genre

-- find authors which didnt sell any books
SELECT 
    a.id
  , a.name
  , a.last_name
  , a.nationality
FROM
    author a
    LEFT JOIN books b ON a.id = b.author_id
WHERE
    b.book_id IS NULL
;


-- Salaries with columns employee_id, salary, and effective_date. 
-- Write a query to find the previous salary of each employee
-- The result should include employee_id, salary, previous_salary, and effective_date.

SELECT 
    employee_id
  , salary 
  , LAG(salary) OVER (PARTITION BY employee_id ORDER BY efective_date asc)  AS previous_salary
  , effective_date
FROM 
    salaries
;

-- Given a table orders with columns order_id, customer_id, order_amount, and order_date
-- write a query to find the difference between the current order amount and the previous order amount for each customer. 
-- Include customer_id, order_id, order_date, order_amount, and amount_diff.
SELECT 
    customer_id,
    order_id, 
    order_date,
    order_amount,
    order_amount - LAG(order_amount) OVER (PARITION BY customer_id ORDER BY order_date) AS amount_diff 
FROM 
    orders
;

-- Given a table stock_prices with columns stock_id, price, and price_date, write a query to find the price difference between the 
-- current day and the previous day for each stock. Include stock_id, price_date, price, and price_diff.
SELECT 
    stock_id, 
    price, 
    price_date, 
    price - LAG(price) OVER(partition by stock_id ORDER BY price_date) AS price_diff
FROM 
    stock_prices
;

-- Given a table appointments with columns appointment_id, patient_id, and appointment_date, write a query to find the next appointment 
-- date for each patient. Include patient_id, appointment_id, appointment_date, and next_appointment_date.
SELECT 
    patient_id, 
    appointment_id, 
    appointment_date, 
    LEAD(appointment_date) OVER (PARTITION BY patient_id ORDER BY appointment_date) next_appointment_date
FROM 
    appoitments
;

-- Given a table monthly_sales with columns month, sales_amount, and store_id, write a query to calculate the cumulative sales amount 
-- and the difference from the previous month's sales for each store. Include store_id, month, sales_amount, cumulative_sales, and 
-- sales_diff.
SELECT 
    store_id, 
    month, 
    sales_amount, 
    sales_amount - LAG(sales_amount) OVER(PARTITION BY store_id ORDER BY month) sales_diff,
    SUM(sales_amount) OVER(PARTITION BY store_id ORDER BY month) cumulative_sales
FROM 
    monthly_sales
;