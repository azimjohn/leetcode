from itertools import zip_longest

class Solution:
def addStrings(num1, num2):
    carry = 0
    result = ""
    num1, num2 = reversed(num1), reversed(num2)

    for c1, c2 in zip_longest(num1, num2, fillvalue="0"):
        d1, d2 = int(c1), int(c2)
        sum_ = d1 + d2 + carry
        carry = sum_ // 10
        result = str(sum_ % 10) + result

    if carry:
        result = str(carry) + result

    return result
