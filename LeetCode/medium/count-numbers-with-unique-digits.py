class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        n = min(n, 10) # if n >= 10, is invalid
        f = [0] * 11
        dp = [0] * 11

        dp[0] = 1
        dp[1] = 10
        f[0] = 1
        f[1] = 9

        for i in range(2, n + 1):
            f[i] = f[i-1] * (11 - i)
            dp[i] = dp[i-1] + f[i]
        return dp[n]
