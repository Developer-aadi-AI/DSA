# Write your MySQL query statement below
-- select 
--     contest_id,
--     round((count(u.user_id)/ (SELECT COUNT(*) FROM Users)  * 100, 2) as percentage,  
-- from 
--     Users u inner join Register r 
-- On
--     u.user_id = r.user_id
-- Group by
--     contest_id
-- order by percentage and contest_id;

SELECT 
    contest_id,
    ROUND(
        (COUNT(r.user_id) * 100.0 / (SELECT COUNT(*) FROM Users)),
        2
    ) AS percentage
FROM Register r
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;