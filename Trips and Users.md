### Problem Statement(https://leetcode.com/problems/trips-and-users/description/):

Table: Trips

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| client_id   | int      |
| driver_id   | int      |
| city_id     | int      |
| status      | enum     |
| request_at  | varchar  |     
+-------------+----------+
id is the primary key (column with unique values) for this table.
The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
Status is an ENUM (category) type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').
Table: Users

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| users_id    | int      |
| banned      | enum     |
| role        | enum     |
+-------------+----------+
users_id is the primary key (column with unique values) for this table.
The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
banned is an ENUM (category) type of ('Yes', 'No').
The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03" with at least one trip. Round Cancellation Rate to two decimal points.

====================================================================================

### Solution:
    select request_at as Day, Round(SUM(CASE WHEN status like 'cancelled%' THEN 1 ELSE 0 END)/count(*), 2) as         "Cancellation Rate"
    from Trips
    where TO_DATE(request_at, 'YYYY-MM-DD') between DATE '2013-10-01' and DATE '2013-10-03'
    and client_id not in (select users_id from Users where banned = 'Yes' and role = 'client')
    and driver_id not in (select users_id from Users where banned = 'Yes' and role = 'driver')
    group by request_at
    order by request_at
