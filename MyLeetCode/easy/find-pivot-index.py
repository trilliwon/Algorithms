class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        [1, 7, 3, 6, 5, 6]
                  ^
         right = [5, 6]
         left = 11
         pivot = 3*
         pivot val = 6
        """
        
        right = sum(nums)
        left = 0
        
        for i, x in enumerate(nums):
            pivot = i
            right -= x
            if left == right:
                return i
            left += x
        return -1
