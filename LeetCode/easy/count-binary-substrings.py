class Solution:
    
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        comp = []
        counter = 0
        for i in range(1, len(s) + 1):
            if i < len(s) and s[i-1] == s[i]:
                counter += 1
            else:
                comp.append(counter + 1)
                counter = 0

        ans = 0
        for i in range(1, len(comp)):
            a = comp[i-1]
            b = comp[i]
            ans +=  min(a, b) if a != b else a
        return ans
