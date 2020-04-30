# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        try:
            index = inorder.index(root.val)
        except ValueError:
            return None

        left, right = inorder[:index], inorder[index+1:]

        root.left = self.buildTree(preorder[1:index+1], left)
        root.right = self.buildTree(preorder[index+1:], right)

        return root


if __name__ == '__main__':
    s = Solution()
    s.buildTree([3, 20, 15, 7], [3, 15, 20, 7])
