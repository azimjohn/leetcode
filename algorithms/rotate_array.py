class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length
        
        numsRotated = nums[length - k:] + nums[:length - k]
        
        for i in range(length):
            nums[i] = numsRotated[i]
