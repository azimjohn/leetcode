class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        differences = 0

        while xor:
            differences += xor & 1
            xor = xor >> 1

        return differences
