class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_leght_str = min(strs, key=lambda s: len(s))
        prefix_index = 0
    
        for i in range(len(min_leght_str)):
            ith_letters = [string[i] for string in strs]
            
            if len(set(ith_letters)) != 1:
                break
            
            prefix_index += 1
        
        return min_leght_str[:prefix_index]
