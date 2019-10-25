# https://leetcode.com/submissions/detail/273110692/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    
    if not p or not q:
        return False

    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)

    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(4)

    print("PASS" if is_same_tree(t1, t1) is True else "FAIL")
    print("PASS" if is_same_tree(t2, t1) is False else "FAIL")
