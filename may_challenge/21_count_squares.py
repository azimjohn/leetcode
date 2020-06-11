class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        result = 0
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        result += 1
                    else:
                        val = matrix[i][j] + min(
                            matrix[i-1][j-1],
                            matrix[i][j-1],
                            matrix[i-1][j]
                        )
                        result += val
                        matrix[i][j] = val
        return result
