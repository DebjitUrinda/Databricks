### Problem Statement ():

Table: RequestAccepted

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
 

Write a solution to find the people who have the most friends and the most friends number.

===========================================================================================

### SOLUTION:
    select t.id, sum(t.num) as num from (select distinct requester_id as id, count(*) as num from RequestAccepted group by requester_id
    union all
    select distinct accepter_id as id, count(*) as num from RequestAccepted group by accepter_id) t
    group by t.id
    order by num desc
    limit 1
