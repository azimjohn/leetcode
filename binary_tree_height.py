# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    if not root:
        return 0
        
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("PASS" if maxDepth(root) == 3 else "FAIL")
