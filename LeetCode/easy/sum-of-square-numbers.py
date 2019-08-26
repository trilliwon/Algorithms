class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        """
        3**2 + 4**2 = 25
        """

        for i in range(int(math.sqrt(c))+1):
            b = math.sqrt(c - i**2)
            if b - int(b) == 0.0:
                return True
        return False
# https://leetcode.com/problems/sum-of-square-numbers/solution/            
