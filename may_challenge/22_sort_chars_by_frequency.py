from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        result = ''
        counter = Counter(s)

        for char in sorted(counter, key=lambda k: -counter[k]):
            result += char * counter[char]

        return result
