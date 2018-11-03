class Solution:
    
    def dfs(self, grid, start):
        """
        :type start (int, int)
        """
        pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        stack = []
        stack.append(start)
        print(start)
        grid[start[0]][start[1]] = -1
        ans = 1
        
        while stack:
            curr = stack.pop()
            for x, y in pos:
                nx = curr[0] - x
                ny = curr[1] - y
                if nx >= 0 and ny >= 0 and nx < len(grid) and  ny < len(grid[0]) and grid[nx][ny] == 1:
                    stack.append((nx, ny))
                    grid[nx][ny] = -1
                    ans += 1
        return ans
        
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, (i, j)))
        return ans
