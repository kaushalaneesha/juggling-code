CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      WITH ranked_salary AS (
        SELECT 
            salary, 
            dense_rank() over(order by salary desc) as d_rank
        from 
            employee
        )
        SELECT (
            IFNULL (
                (SELECT 
                    DISTINCT salary from ranked_salary where d_rank = N
                ), NULL
            )
        ) 
  );
END