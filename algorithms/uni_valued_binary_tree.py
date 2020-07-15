# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return True
        return self.dfs(root, root.val)

    def dfs(self, root: TreeNode, val: int):
        if not root: return True
        return (
            root.val == val and \
            self.dfs(root.left, val) and \
            self.dfs(root.right, val)
        )
