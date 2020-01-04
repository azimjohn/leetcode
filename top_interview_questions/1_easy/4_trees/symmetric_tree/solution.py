# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_symmetric(left, right):
    if not left and not right:
        return True

    if not left or not right:
        return False

    return left.val == right.val and is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(3)
    t1.left.right = TreeNode(4)
    t1.right.left = TreeNode(4)
    t1.right.right = TreeNode(3)

    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(2)
    t2.left.right = TreeNode(3)
    t2.right.right = TreeNode(3)

    assert is_symmetric(t1, t1) is True
    assert is_symmetric(t2, t2) is False
