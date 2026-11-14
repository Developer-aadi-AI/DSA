# Write your MySQL query statement below
select id 
    from (select 
        id,
        temperature, 
        recordDate,
        lag(temperature) over (order by recordDate) as prevtemp, 
        lag(recordDate) over (order by recordDate) as prevdate 
        from Weather) 
    as temp 
    where temperature > prevtemp and datediff(recordDate, prevdate) = 1;