class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
    
        h = len(matrix)
        w = len(matrix[0])
        answer = 0

        for i in range(h):
            for j in range(w):
                x, y = i, j
                
                while x < h and y < w:
                    flag = True

                    if matrix[i][j] == '0':
                        break

                    for k in range(i, x + 1):
                        if matrix[k][y] == '0':
                            flag = False
                            break

                    if not flag:
                        break

                    for k in range(j, y + 1):
                        if matrix[x][k] == '0':
                            flag = False
                            break

                    if not flag:
                        break
                    x, y = x + 1, y + 1

                answer = max((x - i) * (y - j), answer)
        return answer
