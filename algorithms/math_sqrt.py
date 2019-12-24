class Solution:
    def mySqrt(self, a: int) -> int:
        if a == 0:
            return 0
        
        x = a
        for _ in range(25):
            x = 0.5 * (x + a / x)
        
        return int(x)
