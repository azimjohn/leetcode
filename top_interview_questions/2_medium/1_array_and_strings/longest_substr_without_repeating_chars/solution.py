class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = 1
        length = len(s)
        dict_ = dict()
        i, j = 0, 0

        while j < length:
            char = s[j]
            if char in dict_:
                i = max(i, dict_[char])

            longest = max(longest, j - i + 1)
            dict_[char] = j + 1
        
            j += 1

        return longest
