class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_ = 0

        for _ in range(32):
            reversed_ = reversed_ << 1
            reversed_ += (n & 1)
            n = n >> 1

        return reversed_

