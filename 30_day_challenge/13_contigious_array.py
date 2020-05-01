class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_contiguous = 0
        first_occurances = {0: -1}
        sum_ = 0

        for i, num in enumerate(nums):
            if num == 0:
                sum_ -= 1
            else:
                sum_ += 1
            
            if sum_ not in first_occurances:
                first_occurances[sum_] = i
                continue

            max_contiguous = max(i - first_occurances[sum_], max_contiguous)
        
        return max_contiguous
