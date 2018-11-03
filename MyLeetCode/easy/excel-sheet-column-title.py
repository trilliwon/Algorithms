class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        ans = ''
        while n != 0:
            n -= 1
            digit = n % 26
            ans = chr(ord('A') + digit) + ans
            n = n // 26
        return ans
