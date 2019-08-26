class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        m = len(S)
        ans = [m for _ in range(m)]
        for i in range(m):
            if S[i] == C:
                ans[i] = 0
                
        # [m, m, m, 0, m, 0, 0, m, m, m, m, 0]
        
        for i in range(1, m):
            if ans[i] > ans[i-1]:
                ans[i] = ans[i-1] + 1

        for i in range(m-1, 0, -1):
            if ans[i] < ans[i-1]:
                ans[i-1] = ans[i] + 1
        return ans
