class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = self.getSquareRoot(num) 
        return num == root * root

    def getSquareRoot(self, num: int) -> int:
        result = num
        
        for _ in range(100):
            result = 0.5 * (result + num/result)
        
        return int(result)
