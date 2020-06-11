class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance_squared = point[0]**2 + point[1]**2
            heapq.heappush(heap, (distance_squared, point))

        k_closest = heapq.nsmallest(K, heap)

        return [point for _, point in k_closest]
