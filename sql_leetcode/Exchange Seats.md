### Problem Statement (https://leetcode.com/problems/exchange-seats/description/):

Table: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.
 

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

======================================================================

### SOLUTION:
    select (case when mod(id, 2) <> 0 and id <> (select max(id) from Seat) then id+1
                 when mod(id, 2) = 1 then id
                 else id-1
            end) as id,
        student from Seat
        order by id
