class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = list(filter(lambda c: c != '-', S.upper()))
        S.reverse()
        answer = []

        for i in range(len(S)):
            if i % K == 0 and i != 0:
                answer.append('-')
            answer.append(S[i])

        answer.reverse()
        return ''.join(answer)

        
