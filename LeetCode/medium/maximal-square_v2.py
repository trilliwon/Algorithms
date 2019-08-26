class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
    
        h = len(matrix)
        w = len(matrix[0])

        answer = 0

        cache = [[0 for _ in range(w)] for _ in range(h)]

        for i in range(h):
            if matrix[i][0] == '1':
                answer = 1
                cache[i][0] = 1

        for j in range(w):
            if matrix[0][j] == '1':
                answer = 1
                cache[0][j] = 1

        for i in range(1, h):
            for j in range(1, w):
                if matrix[i][j] == '1':
                    cache[i][j] = min(cache[i-1][j], cache[i][j-1], cache[i-1][j-1]) + 1
                    answer = max(answer, cache[i][j])
        return answer ** 2
