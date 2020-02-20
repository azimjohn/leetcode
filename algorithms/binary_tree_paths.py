
# https://leetcode.com/problems/binary-tree-paths/
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.result = []
        self.helper(root, "")
        return self.result
    def helper(self, root: TreeNode, prev_path: str) -> List[str]:
        if not root:
            return
        path = f"{prev_path}->{root.val}" if prev_path else f"{root.val}"
        if not root.left and not root.right:
            self.result.append(path)
        self.helper(root.left, path)
        self.helper(root.right, path)
