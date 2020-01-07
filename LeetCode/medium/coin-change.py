from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if n == 0:
            return 0

        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i and dp[i-coin] != -1:
                    if dp[i] == -1:
                        dp[i] = 1 + dp[i-coin]
                    else:
                        dp[i] = min(dp[i], 1 + dp[i-coin])

        return dp[-1]
