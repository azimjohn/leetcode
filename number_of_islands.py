class Solution:
    neighbours = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        count = 0
        visited = [[False for row in column] for column in grid]
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs(grid, i, j, visited)
                    count += 1

        return count

    def dfs(self, grid, i, j, visited):
        if not self.in_border(grid, i, j) or visited[i][j] or grid[i][j] == '0':
            return

        visited[i][j] = True
        for neighbour in self.neighbours:
            self.dfs(grid, i + neighbour[0], j + neighbour[1], visited)

    def in_border(self, grid, i, j):
        if i < 0 or j < 0:
            return False

        if i >= len(grid) or j >= len(grid[0]):
            return False

        return True
