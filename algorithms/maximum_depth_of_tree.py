"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    cache = {}
    
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        if not root.children:
            return 1
        
        if root in self.cache:
            return cache[root]
        
        result = max([self.maxDepth(c) for c in root.children]) + 1
        self.cache[root] = result
        
        return result
