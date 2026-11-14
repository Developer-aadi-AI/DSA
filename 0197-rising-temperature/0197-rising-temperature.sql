# Write your MySQL query statement below
-- select id 
--     from (select 
--         id,
--         temperature, 
--         recordDate,
--         lag(temperature) over (order by recordDate) as prevtemp, 
--         lag(recordDate) over (order by recordDate) as prevdate 
--         from Weather) 
--     as temp 
--     where temperature > prevtemp and datediff(recordDate, prevdate) = 1;

select w1.id
from Weather w1 inner join Weather w2
on w1.recordDate = w2.recordDate + interval 1 day
where w1.temperature > w2.temperature;