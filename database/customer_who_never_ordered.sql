# https://leetcode.com/problems/customers-who-never-order/submissions/

-- SELECT customers.Name as Customers FROM customers WHERE customers.Id NOT IN (
--    SELECT orders.CustomerId FROM orders
-- )

SELECT customers.Name as Customers FROM customers 
LEFT JOIN orders ON customers.Id = orders.CustomerId
WHERE orders.Id is NULL;
