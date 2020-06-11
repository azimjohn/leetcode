class Graph:
    def __init__(self, size) -> None:
        self.size = size
        self._graph = collections.defaultdict(list)

    def addEdge(self, course: int, requirement: int) -> None:
        self._graph[course].append(requirement)

    def hasCycle(self) -> bool:
        rec_stack = set()
        visited = set()

        for vertex in range(self.size):
            if vertex in visited:
                continue

            if self._isCyclic(vertex, rec_stack, visited):
                return True

        return False

    def _isCyclic(self, vertex, rec_stack, visited):
        rec_stack.add(vertex)
        visited.add(vertex)

        for requirement in self._graph[vertex]:
            if requirement not in visited:
                if self._isCyclic(requirement, rec_stack, visited):
                    return True
            elif requirement in rec_stack:
                return True

        rec_stack.remove(vertex)
        return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = Graph(numCourses)

        for course, requirement in prerequisites:
            graph.addEdge(course, requirement)

        return not graph.hasCycle()
