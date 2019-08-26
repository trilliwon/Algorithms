class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        perms = self.permuteUnique(nums[1:])
        first = nums[0]
        result = []
        for perm in perms:
            for i in range(len(perm) + 1):
                temp = perm[:i] + [first] + perm[i:]
                if temp not in result:
                    result.append(temp)
        return result
