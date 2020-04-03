class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # no need to sort with nlogn.
        # instead use heap to find 3 max and 3 min nums.
        nums.sort()

        if nums[0] <= nums[1] < 0:
            negative = nums[0] * nums[1] * nums[-1]
            positive = nums[-1] * nums[-2] * nums[-3]
            
            return max(negative, positive)
        
        return nums[-1] * nums[-2] * nums[-3]
