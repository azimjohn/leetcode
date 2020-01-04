MAX_INT = 2147483647
MIN_INT = -2147483648


class Solution:
    def myAtoi(self, string: str) -> int:
        string = string.strip()

        if not string:
            return 0

        if not (string[0] in ('-', '+') or string[0].isdigit()):
            return 0

        digit_end_position = 1
        for index, char in enumerate(string[1:], 2):
            if not char.isdigit():
                break

            digit_end_position = index

        try:
            result = int(string[:digit_end_position])
        except ValueError:
            result = 0

        if result > MAX_INT:
            return MAX_INT

        if result < MIN_INT:
            return MIN_INT

        return result

