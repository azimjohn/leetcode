class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 2:
            return True
        
        first, last = coordinates[0], coordinates[-1]
        if first[0] == last[0]:
            for coordinate in coordinates:
                if coordinate[1] != first[1]:
                    return False
            return True
        
        # y = k*x + b
        k = (first[1] - last[1]) / (first[0] - last[0])
        b = first[1] - k * first[0]
        
        for coordinate in coordinates:
            if  (k * coordinate[0] + b) != coordinate[1]:
                return False
        
        return True
