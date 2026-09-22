### Problem Statement (https://leetcode.com/problems/employees-earning-more-than-their-managers/):

Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

====================================================================================

### SOLUTION:

select e1.name as Employee
from employee e1
join employee e2
on e1.managerId = e2.id
where e1.salary>e2.salary
