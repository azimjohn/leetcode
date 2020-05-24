class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)

        return nums[length // 2]
