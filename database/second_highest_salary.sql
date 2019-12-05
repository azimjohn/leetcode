# https://leetcode.com/problems/second-highest-salary/submissions/
# Write your MySQL query statement below
SELECT MAX(Salary) AS SecondHighestSalary 
FROM Employee
WHERE Salary < (
    SELECT MAX(SALARY) FROM Employee
)
