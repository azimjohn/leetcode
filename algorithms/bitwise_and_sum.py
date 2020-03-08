class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        m, n = bin(m)[2:], bin(n)[2:]

        if len(m) != len(n):
            return 0

        result = ""
        for i, j in zip(m, n):
            if i != j:
                break

            result += str(i)

        result += "0" * (len(m) - len(result))

        return int(result, 2)
