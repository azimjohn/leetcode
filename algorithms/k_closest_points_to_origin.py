import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def distance_squared(point):
            return point[0] ** 2 + point[1] ** 2

        return heapq.nsmallest(K, points, key=distance_squared)
