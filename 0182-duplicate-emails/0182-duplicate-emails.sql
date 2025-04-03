/* Write your PL/SQL query statement below */
select distinct email from Person where email in (select email from Person group by email having count(email)>1);