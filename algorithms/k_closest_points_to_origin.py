import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points_by_distance_squared = []
        
        for point in points:
            distance_squared = point[0] ** 2 + point[1] ** 2
            points_by_distance_squared.append((distance_squared, point))
        
        k_closest = heapq.nsmallest(K, points_by_distance_squared)
        
        return [element[1] for element in k_closest]
