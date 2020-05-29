from typing import List

class Graph:
    def __init__(self, vertex_count: int, edges: List[List[int]]):
        self.vertex_count = vertex_count
        self.adj_list = [set() for _ in range(vertex_count)]
        
        for edge in edges:
            self.adj_list[edge[0]].add(edge[1])


def find_sink_of_graph(graph: Graph) -> int:
    trusts_no_one = []
    for i in range(graph.vertex_count):
        if len(graph.adj_list[i]) == 0:
            trusts_no_one.append(i)

    for i in trusts_no_one:
        all_trusts = True
        for vertex in range(graph.vertex_count):
            if vertex != i and i not in graph.adj_list[vertex]:
                all_trusts = False
                break
        if all_trusts:
            return i

    return -2


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        for edge in trust:
            edge[0] -= 1
            edge[1] -= 1

        graph = Graph(N, trust)

        return find_sink_of_graph(graph) + 1
