class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = bisect.bisect_left(nums, target)
        if nums[index % len(nums)] == target:
            return index
        return -1
