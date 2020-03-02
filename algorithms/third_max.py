import heapq
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        three_largest = heapq.nlargest(3, set(nums))

        if len(three_largest) < 3:
            return three_largest[0]

        return three_largest[2]


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([3, 2, 1], 1),
        ([1, 2], 2),
        ([2, 2, 3, 1], 1),
    ]

    for case in cases:
        print(s.thirdMax(case[0]), case[1])
        print("PASS" if s.thirdMax(case[0]) == case[1] else "FAIL")
