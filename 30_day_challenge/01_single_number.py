# https://leetcode.com/problems/single-number/submissions/

class Solution:
    def singleNumber(self, numbers: List[int]) -> int:
        xor_sum = 0
        
        for number in numbers:
            xor_sum = xor_sum ^ number
        
        return xor_sum
