from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)
        if total < S:
            return 0
        total += S

        if total % 2 == 1:
            return 0

        total //= 2

        dp = [0] * (total + 1)
        dp[0] = 1

        for x in nums:
            for i in reversed(range(x, total + 1)):
                dp[i] += dp[i-x]

        return dp[total]
