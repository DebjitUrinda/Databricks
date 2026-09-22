### Problem Statement (https://leetcode.com/problems/product-price-at-a-given-date/description/):

Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.
Initially, all products have price 10.

Write a solution to find the prices of all products on the date 2019-08-16.

================================================================================

### SOLUTION:
    SELECT p.product_id,
           COALESCE(t.new_price, 10) AS price
    FROM (
        SELECT DISTINCT product_id
        FROM Products
    ) p
    LEFT JOIN (
        SELECT product_id,
               new_price,
               RANK() OVER (
                   PARTITION BY product_id
                   ORDER BY change_date DESC
               ) AS rnk
        FROM Products
        WHERE change_date <= '2019-08-16'
    ) t
    ON p.product_id = t.product_id
    AND t.rnk = 1;
