# DP MEDIUM
class Solution:
    def numTrees(self, n: int) -> int:
        result = [0 for _ in range(n+1)]
        result[0] = 1
        result[1] = 1

        for x in range(1, n + 1):
            s = 0
            x -= 1
            for i in range(x + 1):
                s += (result[x-i] * result[i])
            result[x+1] = s

        return result[n]
