class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        color = image[sr][sc]
        self.inplaceFloodFill(image, sr, sc, newColor, color, visited)
    
        return image

    def inplaceFloodFill(
        self, 
        image: List[List[int]], 
        sr: int, sc: int, 
        newColor: int,
        color: int,
        visited: set
    ):
        print(sr, sc)
        if (sr, sc) in visited:
            return
        
        image[sr][sc] = newColor
        visited.add((sr, sc))

        if sr + 1 < len(image) and image[sr+1][sc] == color:
            self.inplaceFloodFill(image, sr+1, sc, newColor, color, visited)
        
        if sc + 1 < len(image[0]) and image[sr][sc+1] == color:
            self.inplaceFloodFill(image, sr, sc+1, newColor, color, visited)
        
        if sr - 1 >= 0 and image[sr-1][sc] == color:
            self.inplaceFloodFill(image, sr-1, sc, newColor, color, visited)
        
        if sc - 1 >= 0 and image[sr][sc-1] == color:
            self.inplaceFloodFill(image, sr, sc-1, newColor, color, visited)
