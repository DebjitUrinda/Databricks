### Problem Statement (https://leetcode.com/problems/combine-two-tables/description/):
Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

=================================================================================

**NOTE**: Left join korle driver ta left e thakbe, and this is faster sometimes depending on the way data in scanned under the hood, jodi driver table ta agey scan hoy then left join korle agey pawa jabe and execution will be faster.

=================================================================================

### INVARIANT

=================================================================================

### SOLUTION
-- Write your PostgreSQL query statement below
select p.firstName, p.lastName, a.city, a.state
from person p
left join address a
on p.personId = a.personId
