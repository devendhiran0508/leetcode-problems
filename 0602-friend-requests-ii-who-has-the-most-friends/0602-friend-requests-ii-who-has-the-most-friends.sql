# Write your MySQL query statement below
with friend as (select requester_id as id from RequestAccepted union all select accepter_id as id from RequestAccepted)
select id,count(*)as num from friend group by 1 order by 2 desc limit 1;