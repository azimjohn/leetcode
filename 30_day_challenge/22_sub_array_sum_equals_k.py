class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        sum_ = 0
        dict_ = {0: 1}
        count = 0
        
        for n in nums:
            sum_ += n
            if (sum_ - k) in dict_:
                count += dict_[sum_ - k]
    
            dict_[sum_] = dict_.get(sum_, 0) + 1
        
        return count

