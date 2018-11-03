class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        originalr = len(nums)
        originalc = len(nums[0])
    
        if r*c != originalr*originalc or r == originalr:
            return nums
        
        traversed = [elem for l in nums for elem in l]

        nums = []
        counter = 0
        for i in range(r):
            nums.append([])
            for j in range(c):
                nums[i].append(traversed[counter])
                counter += 1
        return nums
            
        
