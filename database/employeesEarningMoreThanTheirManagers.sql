select name Employee from Employee e1 
where e1.salary > 
    (select salary from Employee e2 where e2.id=e1.ManagerId);
