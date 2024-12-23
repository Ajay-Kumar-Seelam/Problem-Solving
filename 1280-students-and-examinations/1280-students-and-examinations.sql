# Write your MySQL query statement below


SELECT 
    a.student_id, 
    a.student_name, 
    b.subject_name ,
    Count(c.subject_name) as attended_exams
FROM 
    Students as a join Subjects as b
  left JOIN 
    Examinations as c 
     ON a.student_id = c.student_id 
    and b.subject_name=c.subject_name
     #where c.subject_name IS NOT NULL
    group by a.student_id,b.subject_name 
    order by a.student_id,b.subject_name
    
     
    
;

