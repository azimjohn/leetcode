# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, root, min_, max_):
        if not root:
            return True

        return min_ < root.val < max_ and self.valid(root.left, min_, root.val) and self.valid(root.right, root.val, max_)
