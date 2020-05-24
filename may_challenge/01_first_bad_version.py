# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        min_ = 0
        max_ = n
        
        while min_ < max_:
            middle = (min_ + max_ + 1) // 2
            if isBadVersion(middle):
                max_ = middle
            else:
                min_ = middle
            
            if max_ - min_ == 1:
                if isBadVersion(min_):
                    return min_
                
                return max_

        return middle
