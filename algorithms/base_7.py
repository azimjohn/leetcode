class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        remainders = []
        is_negative = num < 0
        num = abs(num)

        while num:
            remainder = num % 7
            num = num // 7
            remainders.append(str(remainder))

        remainders = reversed(remainders)

        result = "".join(remainders)
        if is_negative:
            result = "-" + result

        return result


if __name__ == '__main__':
    s = Solution()
    cases = [
        (100, "202"),
        (-7, "-10"),
    ]

    for case in cases:
        print("PASS" if s.convertToBase7(case[0]) == case[1] else "FAIL")
