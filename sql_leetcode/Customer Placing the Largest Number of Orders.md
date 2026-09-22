### Problem Statement ():

Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.
 

Write a solution to find the customer_number for the customer who has placed the largest number of orders.

==================================================================================================

### SOLUTION:
    select customer_number from (select customer_number, count(order_number) as cnt from Orders
    group by customer_number
    order by cnt desc
    limit 1) t
