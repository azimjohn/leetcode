# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.levels = []
        self.levelOrder(root)

        for i in range(len(self.levels)):
            if i % 2:
                self.levels[i] = list(reversed(self.levels[i]))

        return self.levels

    def levelOrder(self, root: TreeNode, level=0):
        if not root:
            return

        if len(self.levels) < level + 1:
            self.levels.append([])

        self.levels[level].append(root.val)

        self.levelOrder(root.left, level + 1)
        self.levelOrder(root.right, level + 1)
