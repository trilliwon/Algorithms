# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        left = 1
        right = n

        while left < right:
            mid = (left + right)//2

            checker = guess(mid)
            
            if mid == left:
                if guess(right) == 0:
                    return right

            if checker == -1:
                right = mid
            elif checker == 1:
                left = mid
            else:
                return int(mid)
