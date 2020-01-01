from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for j in range(0, len(nums)):
                if (i - nums[j]) >= 0:
                    dp[i] += dp[i - nums[j]]
        return dp[target]
