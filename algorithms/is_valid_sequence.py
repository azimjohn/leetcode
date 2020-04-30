# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int], is_leaf=False) -> bool:
        if not root and not arr:
            return is_leaf
        
        if not arr:
            return not bool(root)
    
        if not root:
            return False
        
        if root.val != arr[0]:
            return False
        
        is_leaf = not root.left and not root.right
        left_valid = self.isValidSequence(root.left, arr[1:], is_leaf)
        right_valid = self.isValidSequence(root.right, arr[1:], is_leaf)

        return left_valid or right_valid
