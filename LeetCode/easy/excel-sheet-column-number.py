class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ans = 0
        s = s[::-1]
        for i, c in enumerate(s):
            ans = (26**i)*(ord(c) - ord('A') + 1) + ans
        return ans
