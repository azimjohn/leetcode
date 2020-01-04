from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for index in range(len(nums)-1, -1, -1):
            if nums[index] == 0:
                del nums[index]
                nums.append(0)
