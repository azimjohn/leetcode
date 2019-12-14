class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)
        nums = set(nums)

        for i in range(max_num):
            if i not in nums:
                return i
    
        return max_num + 1
