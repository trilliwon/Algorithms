class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[], [nums[0]]]
        
        for i in range(1, len(nums)):
            tempsubsets = [ s for s in subsets]
            for s in tempsubsets:
                subsets.append(s + [nums[i]])
        return subsets
