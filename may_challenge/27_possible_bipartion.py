class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def addEdge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def possibleBipartion(self):
        visited = set([])

        for vertice in self.graph:
            if vertice in visited:
                continue
            group_a, group_b = set(), set()
            self.bfs(vertice, group_a, group_b, visited)

            if group_a.intersection(group_b):
                return False

        return True

    def bfs(self, vertice, group_a, group_b, visited):
        if vertice in visited:
            return

        queue = collections.deque()
        queue.appendleft((vertice, False))

        while queue:
            vertice, swap = queue.pop()
            if vertice in visited:
                continue

            if swap:
                group_a.add(vertice)
            else:
                group_b.add(vertice)

            for child in self.graph[vertice]:
                if swap:
                    group_b.add(child)
                else:
                    group_a.add(child)
                queue.appendleft((child, not swap))

            visited.add(vertice)

    def dfs(self, vertice, group_a, group_b, visited):
        if vertice in visited:
            return
        visited.add(vertice)
        group_a.add(vertice)

        for child in self.graph[vertice]:
            group_b.add(child)
            self.dfs(child, group_b, group_a, visited)


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = Graph()

        for dislike in dislikes:
            graph.addEdge(*dislike)

        return graph.possibleBipartion()
