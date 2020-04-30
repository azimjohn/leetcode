class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 0:
            return 0

        size = n if n > 6 else 6
        dp = [None for _ in range(size)]
        dp[0], dp[1], dp[2] = 0, 1, 2
        dp[3], dp[4], dp[5] = 4, 6, 9

        for i in range(6, n):
            dp[i] = max(dp[i-2] * 2, dp[i-3] * 3, dp[i-5] * 5)

        return dp[n-1]
