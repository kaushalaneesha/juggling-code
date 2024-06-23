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

-- Description:
-- You have two tables, Employees and Projects. The Employees table contains information about employees, and the Projects table contains information about projects assigned to these employees. Some employees might not have any assigned projects.

-- Employees table:
-- employee_id (int)
-- employee_name (varchar)
-- department (varchar)

-- Projects table:
-- project_id (int)
-- project_name (varchar)
-- employee_id (int)
-- start_date (date)
-- end_date (date)

-- Question:
-- Write an SQL query to retrieve all employees along with their project names and project durations. If an employee does not have any assigned projects, return NULL for the project name and duration.
SELECT 
    e.employee_id, 
    e.employee_name, 
    e.department,
    p.name, 
    DATEDIFF(p.end_date, p.start_date)  AS duration
FROM 
    employee e
    LEFT JOIN projects p
    ON e.employee_id = p.employee_id
