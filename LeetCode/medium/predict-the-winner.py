from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [([-1] * len(nums)) for _ in range(len(nums))]

        def winner(nums, s, e, dp):
            if s == e:
                return nums[s]
            if dp[s][e] != -1:
                return dp[s][e]
            a = nums[s] - winner(nums, s + 1, e, dp)
            b = nums[e] - winner(nums, s, e - 1, dp)
            dp[s][e] = max(a, b)

            return dp[s][e]

        return winner(nums, 0, len(nums) - 1, dp) >= 0
