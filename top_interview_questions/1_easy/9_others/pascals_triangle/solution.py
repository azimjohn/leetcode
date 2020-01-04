from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1 for j in range(i)] for i in range(1, numRows + 1)]

        for i in range(2, numRows):
            for j in range(1, i):
                rows[i][j] = rows[i - 1][j - 1] + rows[i - 1][j]

        return rows
