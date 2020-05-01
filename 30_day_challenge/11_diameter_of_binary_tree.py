# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.helper(root) - 1

    def helper(self, root: TreeNode) -> int:
        if not root:
            return 0

        l_height = self.height(root.left)
        r_height = self.height(root.right)
        
        l_diameter = self.helper(root.left)
        r_diameter = self.helper(root.right)
        
        return max(l_height+r_height+1, max(l_diameter, r_diameter))

    def height(self, tree):
        if not tree:
            return 0

        return 1 + max(self.height(tree.left), self.height(tree.right))
