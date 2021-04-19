CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  declare t int;
  set t=N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary from Employee 
      order by salary desc limit t,1
  );
END
