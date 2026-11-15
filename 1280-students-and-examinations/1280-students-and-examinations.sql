# Write your MySQL query statement below
-- student_id, student_name, subject_name, attended_exams 
select 
S.student_id, 
student_name, 
SB.subject_name,
count(E.subject_name) as attended_Exams
from 
Students S cross join Subjects SB 
Left join Examinations E 
ON S.student_id = E.student_id
AND SB.subject_name = E.subject_name
group by
    S.student_id,
    S.student_name,
    SB.subject_name
Order by 
student_id;