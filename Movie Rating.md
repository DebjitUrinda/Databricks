### Problem Statement (https://leetcode.com/problems/movie-rating/):

Table: Movies

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.
Each movie has a unique title.
Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
The column 'name' has unique values.
Table: MovieRating

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date. 
 

Write a solution to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.

========================================================================

### SOLUTION:
    select name as results from (SELECT
        u.name,
        COUNT(*) AS ratings
    FROM Users u
    JOIN MovieRating mr
    ON u.user_id = mr.user_id
    GROUP BY u.user_id, u.name
    order by ratings desc, u.name asc
    limit 1) t1
    union all
    select title from (select m.title, avg(mr.rating) as avg_rat
    from Movies m
    join MovieRating mr
    on m.movie_id = mr.movie_id
    where mr.created_at between '2020-02-01' and '2020-02-29'
    group by m.movie_id, m.title
    order by avg_rat desc, m.title asc
    limit 1) t2
