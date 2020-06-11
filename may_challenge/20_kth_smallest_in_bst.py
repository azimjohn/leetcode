class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        current = root
        stack = []

        i = 0
        while True:
            if current:
                stack.append(current)
                current = current.left
                continue

            if stack:
                current = stack.pop()
                i += 1
                if i == k:
                    return current.val

                current = current.right
                continue

            break
