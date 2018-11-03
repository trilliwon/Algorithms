class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = collections.Counter()
        for c in s:
            counter[c] += 1

        for c in t:
            counter[c] -= 1
                
        for c, v in counter.items():
            if v == -1:
                return c
