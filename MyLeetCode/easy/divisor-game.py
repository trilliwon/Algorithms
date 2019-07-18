class Solution:
    def divisorGame(self, N: int) -> bool:
        
        result = [False for _ in range(N + 1)]
        
        for n in range(2, N + 1):
            for x in range(n - 1, 0, -1):
                if n % x == 0 and result[n - x] == False:
                    result[n] = True
                    break

        return result[N]
