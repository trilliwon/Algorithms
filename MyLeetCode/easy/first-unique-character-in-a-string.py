class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        comp_map = collections.Counter()
        for c in s:
            comp_map[c] += 1

        for i in range(len(s)):
            if comp_map[s[i]] == 1:
                return i
        return -1
                
