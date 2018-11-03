class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m = max(nums)
        index = -1
        for i in range(len(nums)):
            if m == nums[i]:
                index = i
            elif m < nums[i]*2:
                return -1
        return index
