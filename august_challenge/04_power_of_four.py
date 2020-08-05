class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num % 3 == 1 and (num - 1) & num == 0
