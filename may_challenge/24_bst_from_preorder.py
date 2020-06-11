# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        val = preorder[0]
        root = TreeNode(val)
        root.left = self.bstFromPreorder([n for n in preorder if n < val])
        root.right = self.bstFromPreorder([n for n in preorder if n > val])

        return root
