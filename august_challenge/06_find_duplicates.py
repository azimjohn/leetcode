class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        
        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
            nums[abs(num) - 1] = -nums[abs(num) - 1]

        return result
