class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        hw = 0
        
        while n != 0:
            if n % 2 == 1:
                hw += 1
            n //= 2

        return hw
        
