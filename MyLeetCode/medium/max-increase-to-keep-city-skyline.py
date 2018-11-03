class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        transgrid = []
        transgrid = copy.deepcopy(grid)

        tb = []
        lr = []

        tbmax = 0
        lrmax = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                transgrid[j][i] = grid[i][j]

        for l in grid:
            lr.append(max(l))
        for l in transgrid:
            tb.append(max(l))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = min(lr[i], tb[j])

        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum += (grid[i][j] - transgrid[i][j])



        return sum
