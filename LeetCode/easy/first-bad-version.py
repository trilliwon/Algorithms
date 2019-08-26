# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
                
        if isBadVersion(1):
            return 1
        
        left = 1
        right = n
        
        while left < right:
            mid = math.ceil((right + left)/2)

            if right == mid:
                break

            if isBadVersion(mid):
                right = mid
            else:
                left = mid

        return right
