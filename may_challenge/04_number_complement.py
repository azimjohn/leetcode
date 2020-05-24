class Solution:
    def findComplement(self, num: int) -> int:
        return int(
            bin(num)[2:].replace('0', '*').replace('1', '0').replace('*', '1'), 2
        )
