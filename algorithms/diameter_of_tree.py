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

        l_height = self.height(root.left)
        r_height = self.height(root.right)
        
        l_diameter = self.diameterOfBinaryTree(root.left)
        r_diameter = self.diameterOfBinaryTree(root.right)

        return max(l_height+r_height+1, max(l_diameter, r_diameter)) - 1

    def height(self, tree):
        if not tree:
            return 0

        return 1 + max(self.height(tree.left), self.height(tree.right))


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5) 

    print(s.diameterOfBinaryTree(root))
