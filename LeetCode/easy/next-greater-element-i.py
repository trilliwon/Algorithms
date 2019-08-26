class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if len(nums) == 0:
            return []
        
        lastIndex = len(nums)-1
        numsDic = { nums[lastIndex]: -1 }

        for index in range(lastIndex):
            for i in range(index+1, len(nums)):
                if nums[index] < nums[i]:
                    numsDic[nums[index]] = nums[i] 
                    break
        
        return [numsDic[num] if num in numsDic else -1 for num in findNums]
