class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for row in zero_rows:
            for col in range(cols):
                matrix[row][col] = 0
        
        for col in zero_cols:
            for row in range(rows):
                matrix[row][col] = 0

    
