/* Write your PL/SQL query statement below */
select x,y,z, case 
when x+y<=z or x+z<=y or y+z<=x or x<=0 or y<=0 or z<=0 then 'No'
else 'Yes'
end as triangle from Triangle;