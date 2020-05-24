class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        max_sum = curr_sum = nums[0]
        
        for num in nums[1:]:
            curr_sum = max(curr_sum + num, num)

            if curr_sum > max_sum:
                max_sum = curr_sum
        
        return max_sum
