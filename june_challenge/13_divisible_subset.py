class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        nums.sort()
        div_count = [1 for _ in range(n)]
        prev = [-1 for _ in range(n)]
        max_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if div_count[i] < div_count[j] + 1:
                        div_count[i] = div_count[j] + 1
                        prev[i] = j

            if div_count[max_index] < div_count[i]:
                max_index = i

        result = []
        k = max_index
        while k >= 0:
            result.append(nums[k])
            k = prev[k]

        return result
