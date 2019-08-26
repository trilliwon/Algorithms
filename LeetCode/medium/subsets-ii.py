class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subsets = [[], [nums[0]]]
        
        for i in range(1, len(nums)):
            tempsubsets = [ s for s in subsets]
            for s in tempsubsets:
                subsets.append(s + [nums[i]])

        subsets = [tuple(sorted(s)) for s in subsets]
        
        return [list(s) for s in list(set(subsets))]
