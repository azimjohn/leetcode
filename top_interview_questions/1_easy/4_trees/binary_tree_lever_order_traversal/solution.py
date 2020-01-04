# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.levels = []

    def levelOrder(self, root: TreeNode, level=0) -> List[List[int]]:
        if not root:
            return

        if len(self.levels) < level + 1:
            self.levels.append([])

        self.levels[level].append(root.val)

        self.levelOrder(root.left, level + 1)
        self.levelOrder(root.right, level + 1)

        return self.levels
