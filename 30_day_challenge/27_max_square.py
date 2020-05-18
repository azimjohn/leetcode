class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
    
        max_square = 0
        cols, rows = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(rows)] for _ in range(cols)]
        
        for i in range(cols):
            dp[i][0] = int(matrix[i][0])
            max_square = max(max_square, dp[i][0])

        for j in range(rows):
            dp[0][j] = int(matrix[0][j])
            max_square = max(max_square, dp[0][j])

        for i in range(1, cols):
            for j in range(1, rows):
                val = int(matrix[i][j])
                if val != 0:
                    dp[i][j] = min(int(dp[i-1][j]), int(dp[i][j-1]), int(dp[i-1][j-1])) + val
                max_square = max(max_square, dp[i][j])
        
        return max_square * max_square
