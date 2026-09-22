### Problem Statement (https://leetcode.com/problems/restaurant-growth/description/):

Table: Customer

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
| visited_on    | date    |
| amount        | int     |
+---------------+---------+
In SQL,(customer_id, visited_on) is the primary key for this table.
This table contains data about customer transactions in a restaurant.
visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
amount is the total paid by a customer.
 

You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.

Return the result table ordered by visited_on in ascending order.

==============================================================================

### SOLUTION:
    select o.visited_on, o.amount, round(o.amount/7, 2) as average_amount
    from (select  t.visited_on as visited_on, 
            sum(t.roll_amt) over (order by t.visited_on
                               rows between 6 preceding and current row) as amount,
            row_number() over (order by t.visited_on) as rn
    from (select visited_on, sum(amount) as roll_amt
    from Customer
    group by visited_on) t) o
    where o.rn >= 7
