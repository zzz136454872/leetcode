# Write your MySQL query statement below、
select name Customers from customers where not exists(
  select * from orders where customers.id=orders.customerid);
