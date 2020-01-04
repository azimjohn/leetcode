class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = self.countChars(s)
        counter_t = self.countChars(t)

        return counter_s == counter_t

    def countChars(self, s):
        counter = {}

        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

        return counter
