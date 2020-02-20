-- https://leetcode.com/problems/employees-earning-more-than-their-managers/submissions/
SELECT Employee.Name as Employee FROM Employee 
INNER JOIN Employee as Manager ON Employee.ManagerId = Manager.id
WHERE Employee.Salary > Manager.Salary
