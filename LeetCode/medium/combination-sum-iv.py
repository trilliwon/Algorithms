from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)

        def combination(nums, target):
            if dp[target] != -1:
                return dp[target]
            if target == 0:
                return 1
            result = 0
            for n in nums:
                if target - n >= 0:
                    v = combination(nums, target - n)
                    result += v
            dp[target] = result
            return result

        answer = combination(nums, target)
        return answer
