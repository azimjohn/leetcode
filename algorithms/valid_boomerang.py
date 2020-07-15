class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        points = [tuple(point) for point in points]
        if len(set(points)) != 3:
            return False
        
        if points[0][1] == points[1][1] and points[1][1] == points[2][1]:
            return False
        
        if points[0][1] == points[1][1] or points[1][1] == points[2][1]:
            return True 
        
        k1 = (points[0][0] - points[1][0]) / (points[0][1] - points[1][1])
        k2 = (points[1][0] - points[2][0]) / (points[1][1] - points[2][1])
        
        return k1 != k2
