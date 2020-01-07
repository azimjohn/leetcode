from typing import List


# todo: use binary search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_start, right_start = -1, -1

        for i, num in enumerate(nums):
            if num == target:
                left_start = i
                break

        for i, num in enumerate(reversed(nums)):
            if num == target:
                right_start = len(nums) - i - 1
                break

        return [left_start, right_start]
