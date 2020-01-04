class Solution:
    def climbStairs(self, n: int) -> int:
        "Fibonacci"
        a, b = 1, 1

        i = 1
        while i < n:
            i += 1
            a = a + b
            b = a - b

        return a
