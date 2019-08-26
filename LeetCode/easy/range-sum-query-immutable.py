class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sum_array = []
        if len(nums) == 0:
            return
        self.sum_array.append(nums[0])
        
        for i in range(1, len(nums)):
            self.sum_array.append(self.sum_array[i-1] + nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        if i == 0:
            return self.sum_array[j]
        return self.sum_array[j] - self.sum_array[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
