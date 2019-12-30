from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        length = len(nums)
        if length <= 1:
            return nums
        dp = [0] * length
        pa = [-1] * length
        dp[0] = 1

        maxValue = 0
        maxIndex = 0

        for i in range(1, length):
            for j in reversed(range(0, i)):
                if nums[i] % nums[j] == 0 and dp[i] <= dp[j] + 1:
                    pa[i] = j
                    dp[i] = dp[j] + 1
                    if maxValue <= dp[i]:
                        maxValue = dp[i]
                        maxIndex = i

        ret = set()
        index = maxIndex

        while 0 <= index:
            if pa[index] != -1:
                ret.add(nums[index])
                ret.add(nums[pa[index]])
                index = pa[index]
                if pa[index] == -1:
                    break
            else:
                index -= 1
        ret = list(ret)
        if len(ret) == 0:
            return [nums[0]]
        return ret
