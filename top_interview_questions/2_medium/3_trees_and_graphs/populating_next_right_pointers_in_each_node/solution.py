"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def __init__(self):
        self.levels = []

    def connect(self, root: 'Node') -> 'Node':
        self.levelOrder(root)

        for level in self.levels:
            for i in range(len(level)-1):
                level[i].next = level[i+1]

        return root

    def levelOrder(self, root: TreeNode, level=0) -> List[List[int]]:
        if not root:
            return

        if len(self.levels) < level + 1:
            self.levels.append([])

        self.levels[level].append(root)

        self.levelOrder(root.left, level+1)
        self.levelOrder(root.right, level+1)

        return self.levels
