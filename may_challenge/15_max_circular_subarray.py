
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        sum_ = sum(nums)
        return max([
            self.maxSub(nums),
            sum_ + self.maxSub([-num for num in nums[:n-1]]),
            sum_ + self.maxSub([-num for num in nums[1:]]),
        ])

    def maxSub(self, nums):
        n = len(nums)
        start, end = 0, 0
        max_sum = current_sum = nums[0]
        for i in range(1, n):
            if current_sum + nums[i] > nums[i]:
                current_sum = current_sum + nums[i]
                end = i
            else:
                current_sum = nums[i]
                start = end = i

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
