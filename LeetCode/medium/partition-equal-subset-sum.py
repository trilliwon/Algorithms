from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        length = len(nums)

        if S % 2 == 1:
            return False

        target = S // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for x in nums:
            for i in reversed(range(1, target + 1)):
                if i >= x:
                    dp[i] = dp[i] or dp[i - x]

        return dp[target]
