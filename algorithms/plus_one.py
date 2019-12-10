class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        
        for i in range(length-1, -1, -1):
            digit = digits[i]

            if digit == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        
        
        if digits[0] == 0:
            digits = [1] + digits
    
        return digits
