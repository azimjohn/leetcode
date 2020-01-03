class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
    
        return groups.values()
