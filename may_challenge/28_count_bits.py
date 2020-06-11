class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []

        for i in range(num+1):
            result.append(bin(i).count('1'))

        return result
