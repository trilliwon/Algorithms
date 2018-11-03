class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        s = sum(nums[0:k])
        ma = s
        
        for i in range(k, len(nums)):
            s = s + nums[i] - nums[i - k]
            ma = max(ma, s)
        return ma/k
