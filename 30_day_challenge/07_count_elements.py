class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums = set(arr)
        count = 0
        for num in arr:
            if num+1 in nums:
                count += 1
        
        return count
