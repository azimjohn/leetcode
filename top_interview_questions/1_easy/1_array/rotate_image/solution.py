from copy import deepcopy
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        matrix_copy = deepcopy(matrix)

        for i in range(size):
            for j in range(size):
                matrix[j][size-i-1] = matrix_copy[i][j]
