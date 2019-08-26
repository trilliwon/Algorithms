class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        if n/2 == n//2:
            return self.isPowerOfTwo(n//2)
        else:
            return False
