class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        high, low = len(nums) - 1, 0
        
        while low < high:
            middle = (low + high) // 2

            if nums[middle] not in [nums[middle-1], nums[middle+1]]:
                return nums[middle]
            
            count = (high - low) // 2
            if nums[middle] == nums[middle-1]:
                if count % 2 == 0:
                    high = middle - 2
                else:
                    low = middle + 1
            else:
                if count % 2 == 0:
                    low = middle + 2
                else:
                    high = middle - 1
    
            if count == 1:
                if nums[middle] == nums[middle-1]:
                    return nums[middle+1]
                return nums[middle-1]

        return nums[low]
