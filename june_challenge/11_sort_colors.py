class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j, k = 0, n - 1

        for i in range(n):
            if i == k + 1:
                break
            if nums[i] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            elif nums[i] == 2:
                nums[k], nums[i] = nums[i], nums[k]
                k -= 1
