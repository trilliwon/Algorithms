class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        [1, 4, 2, 3]
            ^  ^       
            2
        [1, 4, 2, 5]
            ^  ^
               4

        [3, 4, 2, 3, 7, 8, 9]
               ^

        [5, 1, 2, 3]
        
        [5, 1, 4, 1]
                   
        [1, 4, 2, 1]
        
        [1,5,4,6,7,10,8,9]
             ^
             5
               
        """     
        l = len(nums)
        counter = 0

        for i in range(1, l):
            if nums[i] < nums[i-1]:
                if i+1 < l and i-2 >= 0:
                    f = nums[i+1] < nums[i-1]
                    s = nums[i-2] > nums[i]  
                    if s and f:
                        return False
                    else:
                        counter += 1
                        if counter > 1:
                            return False
                else:
                    counter += 1
                    if counter > 1:
                        return False
                    
        return True
