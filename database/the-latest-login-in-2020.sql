select l1.user_id,l1.time_stamp last_stamp from Logins l1 
where year(l1.time_stamp)=2020 and not exists (
    select * from Logins l2 
    where l1.user_id=l2.user_id 
        and year(l2.time_stamp)=2020 
        and l2.time_stamp>l1.time_stamp
)
