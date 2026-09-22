### Problem Statement ():

Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
 

Write a solution to find the first login date for each player.

================================================================================

### SOLUTION:

**1. Using min():**
  
    SELECT player_id,
       TO_CHAR(MIN(event_date), 'YYYY-MM-DD') AS first_login
    FROM Activity
    GROUP BY player_id;

**2. Using EXISTS:**

    select player_id, TO_CHAR(MIN(event_date), 'YYYY-MM-DD') as first_login 
    from Activity a1
    where not exists (select 1
    from Activity a2
    where a2.player_id = a1.player_id
    and a2.event_date < a1.event_date)
    order by player_id
