from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        most_common = counter.most_common(k)

        return [element[0] for element in most_common]
