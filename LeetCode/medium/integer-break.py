class Solution:
    def integerBreak(self, n: int) -> int:
        temp = [0, 0, 1, 2, 4, 6, 9]
        T = [0] * (n + 1)
        for i in range(0, min(n+1, 7)):
            T[i] = temp[i]

        if n < 7:
            return T[n]

        for i in range(7, n + 1):
            T[i] = T[i-3] * 3
        return T[-1]
