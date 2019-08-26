class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        if num/4 == num//4:
            return self.isPowerOfFour(num//4)
        else:
            return False
