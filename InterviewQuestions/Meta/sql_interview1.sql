
-- Write a query to print author ID who wrote 5 or more Genres ---Test cases passed
SELECT 
    author_id
    COUNT(distinct genre) unique_genre
FROM 
    books
GROUP BY 
    author_id
HAVING 
    unique_genre >= 5
;

--  Sale table contains   ID , tranaction_date , customer ID
--  Customer table contains Id, registered_date
--  xWrite query to find sales percentage per registered_date/transaction_date

SELECT 
    registered_date
  , SUM(CASE WHEN (s.tranaction_date == c.registered_date) THEN 1 ELSE 0)  AS same_day_sale
  , COUNT(*) total_sale
  , (SUM(CASE WHEN (s.tranaction_date == c.registered_date) THEN 1 ELSE 0) * 100) / COUNT(*) AS sale_percentage
FROM 
    sales s
    RIGHT OUTER JOIN customer c -- Right outer join so as to keep roes when user registered but didnt buy anything (for total)
    ON s.customer_id = c.Id
GROUP BY 
    registered_date
    
-- Write a query to find customer who has more than 1 boook and also min , max tranaction_date greater than 3. 
SELECT 
    customer_id
  , COUNT(distinct transaction_id)  unique_books_read
  , min(tranaction_date) oldest_transaction
  , max(transaction_date) newest_transaction
FROM 
    sales
GROUP BY 
    customer_id
HAVING 
    abs(newest_transaction - oldest_transaction) > 3
    AND unique_books_read > 1