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
    a.id IS NULL
;