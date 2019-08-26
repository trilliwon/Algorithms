import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        comp = [nums[0]]

        for x in nums:
            if comp[-1] < x:
                comp.append(x)
            else:
                comp[bisect.bisect_left(comp, x)] = x

        return len(comp)
