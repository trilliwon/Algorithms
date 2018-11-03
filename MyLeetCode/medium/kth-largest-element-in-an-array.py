class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ma = max(nums)
        mi = min(nums)
        
        comp = collections.Counter()
        
        for x in nums:
            comp[x] += 1

        marr = [ma]
        
        for _ in range(k-1):
            tm = mi
            for x in nums:
                if x > tm and x < ma:
                    tm = x
            ma = tm
            for _ in range(comp[ma]):
                marr.append(ma)
        return marr[k-1]

"""
class Solution:

    def partition(self, array, left, right):
        pivotIndex = (left + right) // 2
        pivot = array[pivotIndex]
        array[right], array[pivotIndex] = array[pivotIndex], array[right]
        storeIndex = left - 1

        for i in range(left, right):
            if array[i] <= pivot:
                storeIndex += 1
                array[i], array[storeIndex] = array[storeIndex], array[i]
        array[right], array[storeIndex + 1] = array[storeIndex + 1], array[right]
        return storeIndex + 1

    def select(self, array, left, right, k):
        if left == right: # If the list contains only one element,
            return array[left]

        pivotIndex = self.partition(array, left, right)

        # The pivot is in its final sorted position
        if k == pivotIndex:
            return array[k]
        elif k < pivotIndex:
            return self.select(array, left, pivotIndex - 1, k)
        else:
            return self.select(array, pivotIndex + 1, right, k)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        k = len(nums) - k
        return self.select(nums, 0, len(nums) - 1, k)
"""

