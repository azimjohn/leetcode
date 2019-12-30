class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets_ = [[]]
        
        for num in nums:
            subset = [sub + [num] for sub in subsets_]
            subsets_.extend(subset)
        
        return subsets_
