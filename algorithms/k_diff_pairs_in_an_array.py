class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_counter = collections.Counter(nums)
        result = 0
        
        for num in nums_counter:
            if k < 0:
                continue
    
            if k == 0:
                if nums_counter[num] > 1:
                    result += 1
                continue
    
            if (num + k) in nums_counter:
                result += 1
        
        return result
