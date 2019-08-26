class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        sort and find
        [-4, -3, -2, -7, 8, 2, -3, -1]
                                    ^
        
        """
        
        for x in nums:
            if nums[abs(x)-1] > 0:
                nums[abs(x)-1] *= -1
        
        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans
        
