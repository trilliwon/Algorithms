class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        perms = self.permute(nums[1:])
        first = nums[0]
        result = []
        for perm in perms:
            for i in range(len(perm) + 1):
                result.append(perm[:i] + [first] + perm[i:])
        return result
