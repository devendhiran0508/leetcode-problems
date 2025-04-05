/* Write your PL/SQL query statement below */
select a.name from Employee a inner join Employee b on a.id=b.managerId group by a.id,a.name having count(b.managerId)>=5;