# https://leetcode.com/problems/unique-paths/

class Solution:
    def __init__(self):
        self.cache = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if (m, n) in self.cache:
            return self.cache[(m, n)]
        
        if n ==0 or m == 0:
            return 0
        
        if [m, n] in [[1, 1], [1, 2], [2, 1]]:
            return 1

        result = self.uniquePaths(m, n - 1) + self.uniquePaths(m - 1, n)
        
        self.cache[(m, n)] = result
        
        return result

