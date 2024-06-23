-- Write your MySQL query statement below
WITH ids as(
SELECT 
    requester_id    AS id
FROM 
    RequestAccepted
UNION ALL
SELECT 
    accepter_id     AS id
FROM 
    RequestAccepted
),
friend_count AS (
SELECT 
    id, 
    COUNT(id) AS num, 
    DENSE_RANK() OVER(ORDER BY COUNT(id) DESC) AS rnk
FROM 
    ids
GROUP BY 
    id
)
SELECT id, num from friend_count where rnk = 1;
