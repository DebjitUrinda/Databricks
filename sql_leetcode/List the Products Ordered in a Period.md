### Problem Statement (https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/):

Table: Products

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id is the primary key (column with unique values) for this table.
This table contains data about the company's products.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
This table may have duplicate rows.
product_id is a foreign key (reference column) to the Products table.
unit is the number of products ordered in order_date.
 

Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.

===========================================================================

### SOLUTION:
    select p.product_name, sum(o.unit) as unit
    from Products p
    join Orders o
    on p.product_id = o.product_id
    and o.order_date between '2020-02-01' and '2020-02-29'
    group by p.product_id
    having sum(o.unit) >= 100
