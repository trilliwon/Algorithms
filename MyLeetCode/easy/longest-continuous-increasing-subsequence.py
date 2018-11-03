class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        ans = 0
        counter = 0
        for i in range(1, len(nums)):
            counter += 1
            if nums[i] <= nums[i-1]:
                ans = max(ans, counter)
                counter = 0
        counter += 1
        return max(ans, counter)
