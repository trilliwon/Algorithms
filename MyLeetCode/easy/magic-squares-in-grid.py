class Solution: 
    
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        height = len(grid)
        width = len(grid[0])
        
        if height < 3 or width < 3:
            return 0
        
        """
        grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
        grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
        
        grid[i][j] + grid[i][j+1] + grid[i][j+2]
        grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2]
        grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
        
        grid[i][j] + grid[i+1][j] + grid[i+2][j]
        grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1]
        grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2]
        
        """
        
        model = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ans = 0
        
        for i in range(height-2):
            for j in range(width-2):
                s = 0
                t = []
                for ii in range(i, i+3):
                    for jj in range(j, j+3):
                        t.append(grid[ii][jj])
                
                if model != sorted(t):
                    continue
                
                ans += (15 == grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] and 
                15 == grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] and 
                15 == grid[i][j] + grid[i][j+1] + grid[i][j+2] and 
                15 == grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] and 
                15 == grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] and 
                15 == grid[i][j] + grid[i+1][j] + grid[i+2][j] and 
                15 == grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] and 
                15 == grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2])

                
        return ans
                    
                    
                
                
