from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        jumps = nums[0]

        for num in nums[1:-1]:
            jumps = max(num, jumps - 1)
            if jumps <= 0:
                return False

        return True
