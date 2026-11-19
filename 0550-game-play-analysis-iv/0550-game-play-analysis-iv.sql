# Write your MySQL query statement below
-- SELECT *
-- FROM Activity
-- WHERE event_date IN (
--     SELECT DATE_ADD(MIN(event_date), INTERVAL 1 DAY)
--     FROM Activity
--     GROUP BY player_id
-- )
-- GROUP BY player_id;

SELECT round(count(player_id) * 1.0/ (select count(distinct player_id) from Activity),2) as fraction
FROM Activity a
WHERE event_date = (
    SELECT DATE_ADD(MIN(event_date), INTERVAL 1 DAY)
    FROM Activity b
    WHERE a.player_id = b.player_id
);