/* Write your PL/SQL query statement below */
select a.name as employee from employee a join employee b on a.managerId=b.id where a.salary>b.salary;