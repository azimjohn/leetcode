class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor_sum = start
        for i in range(1, n):
            xor_sum ^= (start + 2*i)
        
        return xor_sum
