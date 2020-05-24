# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        
        queue = collections.deque()
        queue.append((root, 0, None))
        nodes = {}
        
        while queue:
            node, level, parent = queue.popleft()        
            nodes[node.val] = (level, parent)

            if node.left:
                queue.append((node.left, level+1, node))
                
            if node.right:
                queue.append((node.right, level+1, node))

        return nodes[x][0] == nodes[y][0] and nodes[x][1] != nodes[y][1]
