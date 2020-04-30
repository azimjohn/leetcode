class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        if zeros > 1:
            return [0 for _ in nums]
        
        product = 1
        for n in nums:
            if n != 0:
                product = product * n

        if zeros == 1:
            return [0 if n != 0 else product for n in nums]

        for i, n in enumerate(nums):
            nums[i] = int(product / n) 
            
        return nums
