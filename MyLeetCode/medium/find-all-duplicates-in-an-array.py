class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        r = []

        for n in nums:
            index = abs(n) - 1

            if nums[index] < 0:
                r.append(abs(n))
            nums[index] = -nums[index]

        return r
