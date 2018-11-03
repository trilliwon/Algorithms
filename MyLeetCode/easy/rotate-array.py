class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        k = 3
        [1,2,3,4,5,6,7]
        [5,6,7,1,2,3,4]
        """
        comp = [ x for x in nums]
        
        for i in range(len(nums)-k):
            comp[i+k] = nums[i]

        for i in range(k):
            comp[i] = nums[len(nums)-k+i]

        for i in range(len(comp)):
            nums[i] = comp[i]            
