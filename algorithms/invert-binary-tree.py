# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        inverted = TreeNode(root.val)
        if root.left:
            inverted.right = self.invertTree(root.left)

        if root.right:
            inverted.left = self.invertTree(root.right)

        return inverted
