class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = self.counter(nums1)
        nums2_counter = self.counter(nums2)

        result = []
        for num in nums1_counter:
            if num in nums2_counter:
                min_count = min(nums1_counter[num], nums2_counter[num])
                result.extend([num]*min_count)

        return result

    def counter(self, nums):
        nums_counter = {}
        for num in nums:
            if num in nums_counter:
                nums_counter[num] += 1
            else:
                nums_counter[num] = 1

        return nums_counter
