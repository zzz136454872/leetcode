select name Customers from Customers 
where not exists (
    select * from Orders where Orders.CustomerId=Customers.id);
