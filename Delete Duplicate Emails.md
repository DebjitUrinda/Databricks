### Problem Statement (https://leetcode.com/problems/delete-duplicate-emails/description/):

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

====================================================================================

### Solution:

**1. Using correlated NOT IN query:**
  
    delete from Person
    where id not in (select min(id) from Person group by email)

**2. Using EXISTS:**

    DELETE FROM Person p1
    WHERE EXISTS (
      SELECT 1
      FROM Person p2
      WHERE p1.email = p2.email
        AND p2.id < p1.id
    );
