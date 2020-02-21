from itertools import zip_longest

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = ""
        
        for i, d in enumerate(reversed(num1)):
            product = self.multiplyByDigit(d, num2)
            product += "0" * i
            result = self.addStrings(product, result)

        result = result.lstrip("0")
        return result or "0"
    
    def multiplyByDigit(self, d: str, num: str):
        carry = 0
        d = int(d)
        result = ""
        
        for c in reversed(num):
            product = int(c) * d + carry
            carry = product // 10
            result = str(product % 10) + result
        
        if carry:
            result = str(carry) + result
        
        return result

    def addStrings(self, num1, num2):
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
