class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        """
        child i, gi - min size of cookie (possitive)
        cookie j, sj - size of cookie
        should satisfy sj >= gi, cookie j, to child i
        
        g [1,2]
        s [1,2,3]
        """
        
        # sort
        g = sorted(g)
        s = sorted(s)
        
        j = 0 # cookie number
        
        ans = 0

        for gi in g:
            if j == len(s):
                break
            for sj in range(j, len(s)):
                if s[sj] >= gi:
                    ans += 1
                    j = sj + 1
                    break
                
        return ans
