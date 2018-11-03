class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        nOfLines = 1
        lineLen = 0
        
        ab = "abcdefghijklmnopqrstuvwxyz"
        
        m = { ab[i]: widths[i] for i in range(26) }
        
        for c in S:
            if lineLen + m[c] <= 100:
                lineLen += m[c]
            else:
                lineLen = m[c]
                nOfLines += 1
        return [nOfLines, lineLen]

