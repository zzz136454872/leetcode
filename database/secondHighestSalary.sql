# Write your MySQL query statement below

select max(e1.salary) as SecondHighestSalary from employee e1 where 
exists (
    select * from employee e2 where e1.salary < e2.salary
);
