### Problem Statement(https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/):
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

==========================================================================================

### SOLUTION:
    select name from Employee e 
    join (select count(*) as cnt, managerId from Employee
    group by managerId) t
    on e.id = t.managerId
    where t.cnt >= 5
