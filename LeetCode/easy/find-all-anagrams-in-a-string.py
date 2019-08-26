class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        ans = []

        plen = len(p)
        slen = len(s)
        
        if slen < plen:
            return ans

        sCounter = collections.Counter()
        pCounter = collections.Counter()
        
        for c in p:
            pCounter[c] += 1

        for i in range(plen):
            sCounter[s[i]] += 1

        firstIndex = 0

        if sCounter == pCounter:
                ans.append(firstIndex)

        for i in range(plen, slen):
            sCounter[s[firstIndex]] -= 1
            if sCounter[s[firstIndex]] == 0:
                del sCounter[s[firstIndex]]
            sCounter[s[i]] += 1
            firstIndex += 1
            if sCounter == pCounter:
                ans.append(firstIndex)

        return ans
