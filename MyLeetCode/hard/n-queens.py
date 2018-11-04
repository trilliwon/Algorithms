class Solution:
    def solveNQeensUtil(self, N, row, result, pos):
        if N == row:
            one = []
            for _ in range(N):
                one.append(['.' for i in range(N)])
            for p in pos:
                r, c = p[0], p[1]
                one[r][c] = 'Q'
            result.append(list(map(lambda x: ''.join(x), one)))
            return

        for col in range(N):
            foundSafe = True

            for q in range(row):
                if pos[q][1] == col or pos[q][0] - pos[q][1] == row - col or pos[q][0] + pos[q][1] == row + col:
                    foundSafe = False
                    break

            if foundSafe:
                pos[row] = (row, col)
                self.solveNQeensUtil(N, row + 1, result, pos)

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        pos = [()]*n
        self.solveNQeensUtil(n, 0, result, pos)
        return result


