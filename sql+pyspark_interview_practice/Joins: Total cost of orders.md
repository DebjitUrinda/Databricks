Find the total cost of each customer's orders. Output customer's id, first name, and the total order cost. Order records by customer's first name alphabetically.

Tables
customers
orders

=================

select c.id, c.first_name, sum(o.total_order_cost) as sum
from customers c
join
orders o
on c.id = o.cust_id
group by c.id, c.first_name
order by c.first_name
