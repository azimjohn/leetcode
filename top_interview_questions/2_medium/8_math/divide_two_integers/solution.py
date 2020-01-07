import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31
        sign = 1 if dividend * divisor > 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)

        result = dividend / divisor
        result = sign * math.floor(result)

        if result < min_int or result > max_int:
            return max_int

        return result
