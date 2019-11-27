-- https://leetcode.com/problems/duplicate-emails/

SELECT Email from Person
GROUP BY Email
HAVING COUNT(Email) > 1
