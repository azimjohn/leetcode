class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum_: int) -> bool:
        if not root:
            return False  # true would be better I guess

        if not (root.left or root.right):
            return sum_ == root.val

        remaining_sum = sum_ - root.val
        if root.left and self.hasPathSum(root.left, remaining_sum):
            return True

        if root.right and self.hasPathSum(root.right, remaining_sum):
            return True

        return False


if __name__ == "__main__":
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.right = TreeNode(8)
    tree.left.left = TreeNode(11)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)
    tree.left.left.left = TreeNode(7)
    tree.left.left.right = TreeNode(2)

    s = Solution()

    print(s.hasPathSum(tree, 22))
