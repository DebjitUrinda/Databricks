### Problem Statement (https://leetcode.com/problems/top-travellers/):

Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the column with unique values for this table.
name is the name of the user.
 

Table: Rides

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| user_id       | int     |
| distance      | int     |
+---------------+---------+
id is the column with unique values for this table.
user_id is the id of the user who traveled the distance "distance".
 

Write a solution to report the distance traveled by each user.

Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.

================================================================================

### SOLUTION:
    select u.name, coalesce(sum(r.distance), 0) as travelled_distance
    from Users u
    left join Rides r
    on u.id = r.user_id
    group by u.id
    order by travelled_distance desc, name
