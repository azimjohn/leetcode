# https://leetcode.com/problems/power-of-four/submissions/

# todo: can this be done with bithacks?
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        
        if num % 4 != 0 or num == 0:
            return False
        
        return self.isPowerOfFour(num // 4)
