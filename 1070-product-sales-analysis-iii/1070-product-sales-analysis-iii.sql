# Write your MySQL query statement below


SELECT
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM Sales s
JOIN (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) t
ON s.product_id = t.product_id
AND s.year = t.first_year;




-- select 
-- product_id, 
-- min(year) as first_year, 
-- quantity, 
-- price
-- from Sales
-- Group by product_id



-- select 
-- product_id, 
-- year as first_year, 
-- quantity, 
-- price
-- from Sales s
-- where 
-- year = (select Min(year) from Sales where s.product_id = product_id)