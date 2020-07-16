class Graph:
    def __init__(self):
        self._graph = collections.defaultdict(list)

    def add_edge(self, from_, to, price):
        self._graph[from_].append((to, price))

    def dijkstra(self, src, dst, K):
        costs = collections.defaultdict(lambda: float('inf'))
        current_stops = collections.defaultdict(lambda: float('inf'))
        costs[src], current_stops[src] = 0, 0

        heap = []
        heapq.heappush(heap, (src, 0, 0))

        while len(heap) != 0:
            current, price_so_far, stops = heapq.heappop(heap)
            if stops == K + 1:
                continue

            for to, price in self._graph[current]:
                if price+price_so_far < costs[to]:
                    costs[to] = price+price_so_far
                    heapq.heappush(heap, (to, price+price_so_far, stops+1))
                elif stops < current_stops[to]:
                    current_stops[to] = stops
                    heapq.heappush(heap, (to, price+price_so_far, stops+1))

        return -1 if costs[dst] == float("inf") else costs[dst]


#     def bfs(self, src, dst, K):
#         # runs infinitely if graph is cyclic
#         min_price = float('inf')
#         queue = collections.deque()
#         queue.appendleft((src, 0, 0))
#
#         while len(queue) != 0:
#             current, price_so_far, stops = queue.pop()
#             if stops == K + 2:
#                 continue
#
#             if current == dst:
#                 min_price = min(min_price, price_so_far)
#
#             for to, price in self._graph[current]:
#                 queue.appendleft((to, price + price_so_far, stops+1))
#
#         return min_price if min_price != float('inf') else -1


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = Graph()
        for from_, to, price in flights:
            graph.add_edge(from_, to, price)

        return graph.dijkstra(src, dst, K)
