# Write your MySQL query statement below
select round(sum(tiv_2016),2) as tiv_2016 from insurance i1 where
(lat,lon) not in (select lat,lon from insurance i2 where i1.pid!=i2.pid)
and tiv_2015 in (select tiv_2015 from insurance i3 where i1.pid!=i3.pid);