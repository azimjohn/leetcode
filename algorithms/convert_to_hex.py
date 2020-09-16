class Solution:
    def toHex(self, num: int) -> str:
        if num >= 0:
            return hex(num)[2:]
        
        return hex(2**32+num)[2:]
