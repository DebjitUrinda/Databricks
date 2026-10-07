A social platform's growth team wants to understand how often friend requests result in accepted connections. For each date when friend requests were sent, calculate the proportion of those requests that were accepted.

A request is considered accepted when a matching acceptance record exists for the same sender and receiver. If no matching acceptance record exists, treat the request as not accepted. The acceptance may occur on any date after the request was sent.

Exclude dates on which none of the requests sent were accepted.

Output the request date and the acceptance rate, sorted by date in ascending order.
Table
fb_friend_requests

============

select t1.date as date, 
    count(t2.date) * 1.0/count(*) as percentage_acceptance
from fb_friend_requests t1
left join fb_friend_requests t2
on t1.user_id_sender = t2.user_id_sender
and t1.user_id_receiver = t2.user_id_receiver
and t2.action = 'accepted'
where
t1.action = 'sent'
group by t1.date
HAVING COUNT(t2.date) > 0
ORDER BY t1.date;
