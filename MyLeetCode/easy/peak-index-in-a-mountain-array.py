class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(1, len(A)-1):
            j = i-1
            k = i+1
            if A[j] < A[i] and A[i] > A[k]:
                return i
