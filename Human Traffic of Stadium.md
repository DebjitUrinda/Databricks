### Problem Statement (https://leetcode.com/problems/human-traffic-of-stadium/description/):

Table: Stadium

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| visit_date    | date    |
| people        | int     |
+---------------+---------+
visit_date is the column with unique values for this table.
Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
As the id increases, the date increases as well.
 

Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.

Return the result table ordered by visit_date in ascending order.

========================================================================

### SOLUTION:
    WITH islands AS (
        SELECT
            id,
            visit_date,
            people,
            id - ROW_NUMBER() OVER (ORDER BY id) AS island_no
        FROM Stadium
        WHERE people >= 100
    ),
    qualified_islands AS (
        SELECT island_no
        FROM islands
        GROUP BY island_no
        HAVING COUNT(*) >= 3
    )
    
    SELECT
        i.id,
        i.visit_date,
        i.people
    FROM islands i
    JOIN qualified_islands q
        ON i.island_no = q.island_no
    ORDER BY i.visit_date;
