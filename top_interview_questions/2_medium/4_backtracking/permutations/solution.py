from typing import List


# Todo: solve with iteratively
class Solution:
    def __init__(self):
        self.memo = {}

    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)

        if length == 1:
            return [nums]

        if length == 2:
            return [nums, nums[::-1]]

        nums_set = frozenset(nums)
        if nums_set in self.memo:
            return self.memo[nums_set]

        permuted = []
        for i, num in enumerate(nums):
            permutes = self.permute(nums[:i] + nums[i + 1:])
            for permute in permutes:
                permuted.append([num] + permute)

        self.memo[nums_set] = permuted
        return permuted
