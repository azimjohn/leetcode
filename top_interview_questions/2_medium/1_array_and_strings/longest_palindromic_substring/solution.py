class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = self.duplicateChars(s)
        longest = ""
        current = ""
        length = len(s)

        for n in range(0, length):
            i = 0
            while n - i >= 0 and n + i < length - 1:
                if not s[n - i] == s[n + i + 1]:
                    break
                i += 1

            current = s[n - i + 1:n + i + 1]
            longest = max(longest, current, key=len)

        return longest[::2]  # undo the duplicationg

    def duplicateChars(self, s: str) -> str:
        chars = []
        for char in s:
            chars.append(char)
            chars.append(char)

        return ''.join(chars)
