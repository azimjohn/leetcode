# https://leetcode.com/problems/binary-gap/


class Solution:
    def binaryGap(self, N: int) -> int:
        s = bin(N).strip('0b')
        
        if s.count('1') < 2:
            return 0
        
        return len(max(s.split('1'), key=len)) + 1
