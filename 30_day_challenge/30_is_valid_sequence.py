class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root and not arr:
            return False
        
        if not arr:
            return not bool(root)
    
        if not root:
            return False
        
        if root.val != arr[0]:
            return False
        
        is_leaf = not root.left and not root.right
        if is_leaf:
            return len(arr) == 1
    
        left_valid = self.isValidSequence(root.left, arr[1:])
        right_valid = self.isValidSequence(root.right, arr[1:])

        return left_valid or right_valid
