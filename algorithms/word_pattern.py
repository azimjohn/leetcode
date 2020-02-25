class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        pattern_map = {}
        wordset = set()
        words = string.split()

        if len(words) != len(pattern):
            return False

        for char, word in zip(pattern, words):
            if char not in pattern_map and word in wordset:
                return False

            if char not in pattern_map:
                pattern_map[char] = word
                wordset.add(word)
                continue

            if pattern_map[char] != word:
                return False
        
        return True
