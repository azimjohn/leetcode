# https://leetcode.com/problems/factorial-trailing-zeroes/
# Zeros are powers of 10s, 10 is made of 5 and 2

from math import log


def trailingZeroes(n):
    if n < 5:
        return 0

    fives = n // 5

    return fives + trailingZeroes(fives)


if __name__ == "__main__":
    cases = [
        (3, 0),
        (6, 1),
        (50, 12),
    ]

    for case in cases:
        print(trailingZeroes(case[0]))
        print("PASS" if trailingZeroes(case[0]) == case[1] else "FAIL")
