class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        ans = []
        j = 0
        for i in range(len(S)):
            if S[j] != S[i]:
                if (i-j) > 2:
                    ans.append([j, i-1])
                j = i
                
            if i == len(S) - 1:
                if (i-j) >= 2:
                    ans.append([j, i])
                
        return ans
