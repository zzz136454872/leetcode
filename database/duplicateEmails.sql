# Write your MySQL query statement below
select distinct Email from Person p1 
    where exists(select * from Person p2 
        where p1.id!=p2.id and p1.email=p2.email)
