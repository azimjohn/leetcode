from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        result = []
        flip = False

        for i in range(m-1):
            x, y = i, 0
            row = []
            while m > x >= 0 and n > y >= 0:
                row.append(matrix[x][y])
                x -= 1
                y += 1

            if flip:
                row = row[::-1]

            result.extend(row)
            flip = not flip

        for idx, i in enumerate(range(m, m + n)):
            x, y = m - 1, idx
            row = []
            while m > x >= 0 and n > y >= 0:
                row.append(matrix[x][y])
                x -= 1
                y += 1

            if flip:
                row = row[::-1]

            result.extend(row)
            flip = not flip

        return result


if __name__ == '__main__':
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s = Solution()
    print(s.findDiagonalOrder(arr))
