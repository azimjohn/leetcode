class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.validRows(board):
            return False
        
        if not self.validColumns(board):
            return False
        
        if not self.validGrids(board):
            return False

        return True

    def validRows(self, board):
        for row in board:
            if self.containsDuplicate(row):
                return False

        return True

    def validColumns(self, board):
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            
            if self.containsDuplicate(column):
                return False
        
        return True

    def validGrids(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                numbers_in_grid = [
                    board[0+i][0+j], board[0+i][1+j], board[0+i][2+j],
                    board[1+i][0+j], board[1+i][1+j], board[1+i][2+j],
                    board[2+i][0+j], board[2+i][1+j], board[2+i][2+j],
                ]
                if self.containsDuplicate(numbers_in_grid):
                    return False
        
        return True

    @staticmethod
    def containsDuplicate(nums):
        nums = [num for num in nums if num != '.']

        return len(nums) != len(set(nums))
