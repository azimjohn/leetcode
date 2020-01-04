class Solution:
    def reverse(self, x: int) -> int:
        number = int(str(x).strip('-')[::-1]) * (-1 if x < 0 else 1)
        if number > 2 ** 31 or number < -(2 ** 31) - 1:
            return 0

        return number
