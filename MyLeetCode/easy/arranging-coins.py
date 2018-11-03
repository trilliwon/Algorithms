class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        step = 0

        while n > 0:
            step += 1
            n -= step

        if n == 0:
            return step
        return step - 1
