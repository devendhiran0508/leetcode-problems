# Write your MySQL query statement below
select round(count(a1.player_id)/(select count(distinct a2.player_id)from Activity a2),2) as fraction from Activity a1
where (a1.player_id,date_sub(a1.event_date,interval 1 day))in 
(select a3.player_id, min(a3.event_date)from Activity a3 group by a3.player_id);