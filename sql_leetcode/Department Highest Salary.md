### Problem Statement (https://leetcode.com/problems/department-highest-salary/):

Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 

Write a solution to find employees who have the highest salary in each of the departments.

=======================================================================================

### Solution:
    select t.Department, e.name as Employee, t.Salary
    from (select d.id as DeptId, d.name as Department, max(e.salary) as Salary
    from Employee e
    join Department d
    on e.departmentId = d.id
    group by d.id, d.name) t
    join 
    Employee e
    on t.DeptId=e.departmentId
    and t.Salary=e.salary
