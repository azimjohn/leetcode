class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False

        min_ = nums[0]
        middle = None
        
        for num in nums[1:]:
            if min_ > num:
                min_ = num
    
            if middle is None:
                if num > min_:
                    middle = num
                continue
            
            if middle > num > min_:
                middle = num
    
            if num > middle > min_:
                return True
    
        return False
