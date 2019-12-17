import heapq
from collections import Counter


class Solution:
    def frequencySort2(self, s: str) -> str:
        result = ''
        counter = Counter(s)

        for char in sorted(counter, key=lambda k: -counter[k]):
            result += char * counter[char]

        return result
