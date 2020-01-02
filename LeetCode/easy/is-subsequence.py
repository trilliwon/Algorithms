class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)

        if s_length > t_length:
            return False

        if s_length == 0:
            return True

        dp = [False] * (s_length)

        progress = 0
        for j in range(0, s_length):
            for i in range(progress, t_length):
                progress = i + 1
                if s[j] == t[i]:
                    dp[j] = True
                    break

        return dp[s_length - 1]
