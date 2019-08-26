class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        """
        s = "paper"
             01023
        t = "title"
             01023
        """
        
        # s
        comp = {}
        counter = 0
        ss = []
        
        for c in s:
            if not (c in comp):
                comp[c] = counter
                counter += 1
            ss.append(comp[c])

        comp = {}
        counter = 0
        tt = []
        for c in t:
            if not (c in comp):
                comp[c] = counter
                counter += 1
            tt.append(comp[c])
        return ss == tt
        
