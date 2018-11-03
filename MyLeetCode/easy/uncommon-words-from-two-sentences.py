class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        wordsOfA = collections.Counter(A.split(' '))
        wordsOfB = collections.Counter(B.split(' '))

        ans = []
        for key, v in wordsOfA.items():
            if not (key in wordsOfB) and v == 1:
                ans.append(key)
        
        for key, v in wordsOfB.items():
            if not (key in wordsOfA) and v == 1:
                ans.append(key)

        return ans
