-- People you may know
-- create a table
CREATE TABLE user_friendship (
  userid1 VARCHAR,
  userid2 VARCHAR,
  ts DATETIME
);

-- insert some values
INSERT INTO user_friendship VALUES ('Aneesha', 'Nidhi', CURRENT_DATE());
INSERT INTO user_friendship VALUES ('Nidhi', 'Bhavika', CURRENT_DATE());


WITH all_users AS (
    SELECT 
        userid1 AS user_id
    FROM 
        user_friendship
    UNION 

    SELECT 
        userid2 AS user_id
    FROM 
        user_friendship
), not_friends AS (
    SELECT 
        user_id1, 
        user_id 
    FROM 
        user_friendship uf FULL OUTER JOIN 
        all_users au ON 
        uf.userid2 <> au.user_id
)
SELECT * from not_friends;



