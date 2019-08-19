class Solution:
    def numSquares(self, n: int) -> int:
        squares = [x * x for x in range(n + 1)]
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for x in range(2, n + 1):
            dp[x] = min([dp[x - i*i] for i in range(1, int(math.sqrt(x)) + 1)]) + 1
    
        return dp[-1]
