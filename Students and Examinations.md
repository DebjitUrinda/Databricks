### Problem Statement (https://leetcode.com/problems/students-and-examinations/description/):

Table: Students

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.
 

Table: Subjects

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.
 

Table: Examinations

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
 

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.

==============================================================================

### SOLUTION:
    select s.student_id, s.student_name, sub.subject_name, coalesce(count(e.student_id), 0) as attended_exams
    from Students s
    join Subjects sub
    left join Examinations e
    on s.student_id = e.student_id
    and sub.subject_name = e.subject_name
    group by s.student_id, s.student_name, sub.subject_name
    order by s.student_id, sub.subject_name
