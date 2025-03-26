/* Write your PL/SQL query statement below */
select distinct t.id ,case
when t.p_id is null then 'Root'
when c.id is null then 'Leaf'
else 'Inner'
end as type
from tree t left join tree c on t.id=c.p_id;