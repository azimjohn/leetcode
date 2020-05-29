class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in [0, 1]:
            return num

        high, low = num // 2, 0
        
        while low <= high:
            middle = (high + low) // 2
            if middle ** 2 < num:
                low = middle + 1
            elif middle ** 2 > num:
                high = middle - 1
            else:
                return True

        return False
