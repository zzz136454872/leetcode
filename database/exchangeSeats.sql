# Write your MySQL query statement below

select s1.id id, s2.student student from seat s1,seat s2
where s1.id%2=1 and (s2.id=s1.id+1 
or not exists(
    select * from seat s3 where s3.id>s1.id) 
and s1.id=s2.id )
or s1.id%2=0 and s2.id=s1.id-1 
order by s1.id;
