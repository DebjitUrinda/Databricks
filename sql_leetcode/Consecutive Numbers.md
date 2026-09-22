### PROBLEM STATEMENT:
Find all numbers that appear at least three times consecutively.
Return the result table in any order.

====================================================================

**LAG/LEAD Solution:**
    
    SELECT DISTINCT num AS ConsecutiveNums
    FROM (
      SELECT
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev_num,
        LEAD(num, 1) OVER (ORDER BY id) AS next_num
      FROM Logs
    )
    WHERE prev_num = num
    AND next_num = num;

**Gaps/Island concept:**
1. Using group by and row_number difference:

       select num as ConsecutiveNums
        from(select id, num, row_number() over(partition by num order by id) as rn
            from logs) t
        group by num, id-t.rn
        having count(*)>=3

2. Using LAG():

       SELECT DISTINCT num AS ConsecutiveNums
       FROM (
        SELECT num,
               SUM(new_island) OVER (ORDER BY id) AS island_id
        FROM (
            SELECT id,
                   num,
                   CASE
                       WHEN LAG(num) OVER (ORDER BY id) IS NULL THEN 1
                       WHEN LAG(num) OVER (ORDER BY id) <> num THEN 1
                       ELSE 0
                   END AS new_island
            FROM Logs
        )
        )
        GROUP BY num, island_id
        HAVING COUNT(*) >= 3;

**Joins and Self-joins:**

    SELECT DISTINCT l1.num AS ConsecutiveNums
    FROM Logs l1
    JOIN Logs l2
      ON l2.id = l1.id + 1
    JOIN Logs l3
      ON l3.id = l2.id + 1
    WHERE l1.num = l2.num
    AND l2.num = l3.num;
