from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length

        nums_rotated = nums[length - k:] + nums[:length - k]

        for i in range(length):
            nums[i] = nums_rotated[i]
