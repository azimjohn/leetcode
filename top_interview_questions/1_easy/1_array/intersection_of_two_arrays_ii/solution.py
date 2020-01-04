import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = collections.Counter(nums1)
        nums2_counter = collections.Counter(nums2)

        result = []
        for num in nums1_counter:
            if num in nums2_counter:
                min_count = min(nums1_counter[num], nums2_counter[num])
                result.extend([num]*min_count)

        return result
