class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        difference = collections.Counter(ransomNote) - collections.Counter(magazine)
        
        return not difference
