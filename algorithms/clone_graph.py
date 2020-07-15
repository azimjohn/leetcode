# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        visited, copy_map = set(), {}
        queue = collections.deque()

        copy_node_root = Node(node.val)
        copy_map[node] = copy_node_root
        queue.appendleft((copy_node_root, node))

        while len(queue) != 0:
            copy_node, node = queue.pop()
            if node in visited:
                continue

            for neighbor in node.neighbors:
                if neighbor in copy_map:
                    copy_neighbor = copy_map[neighbor]
                else:
                    copy_neighbor = Node(neighbor.val)
                    copy_map[neighbor] = copy_neighbor
                copy_node.neighbors.append(copy_neighbor)
                queue.appendleft((copy_neighbor, neighbor))
            
            visited.add(node)
    
        return copy_node_root
