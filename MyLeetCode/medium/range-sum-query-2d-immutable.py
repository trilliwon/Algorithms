class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0:
            self.dp = []
            return

        width, height = len(matrix[0]), len(matrix)

        self.dp = [[0] * (width + 1) for _ in range(height + 1)]
        
        for i in range(1, height+1):
            for j in range(1, width+1):
                # dp.c = dp.t + dp.l + m.c - d.tl
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] + matrix[i-1][j-1] - self.dp[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if len(self.dp) == 0:
            return 0

        s = self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]

        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
