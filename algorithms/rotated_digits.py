class Solution:
    def rotatedDigits(self, N: int) -> int:
        rotatables = {'2', '5', '6', '9'}
        non_rotatables = {'3', '4', '7'}
        counter = 0
        
        for i in range(1, N+1):
            if any([digit in str(i) for digit in non_rotatables]):
                continue
    
            if any([digit in str(i) for digit in rotatables]):
                counter += 1
        
        return counter
