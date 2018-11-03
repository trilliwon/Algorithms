class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        height = len(grid)
        width = len(grid[0])
        
        ds = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        perimeter = 0

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    oneper = 4
                    for k in range(4):
                        x, y = ds[k][0] + i, ds[k][1] + j
                        if x >= 0 and x < height and y >= 0 and y < width and grid[x][y] == 1:
                            oneper -= 1
                    perimeter += oneper
        return perimeter
