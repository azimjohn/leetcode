# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        self.binaryMatrix = binaryMatrix
        self.rows, self.cols = binaryMatrix.dimensions()
        
        if any(self.getColumnValue(0)):
            return 0

        high, low = self.rows - 1, 0
        while low <= high:
            middle = (low + high + 1) // 2

            if any(self.getColumnValue(middle)):
                high = middle - 1
            else:
                low = middle + 1
            
        if low < self.cols and any(self.getColumnValue(low)):
            return low

        return -1

    def getColumnValue(self, index):
        return tuple(self.binaryMatrix.get(i, index) for i in range(self.rows))
