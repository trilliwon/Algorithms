class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
    
        if len(nums) <= 2:
            return max(nums)
    
        cache = [ 0 for _ in nums]
        cache[0] = nums[0]
        cache[1] = max(nums[1], nums[0])
        
        for i in range(2, len(nums)):
            cache[i] = max((cache[i-2] + nums[i]), cache[i-1])
        print(cache)
        return cache[len(cache)-1]
