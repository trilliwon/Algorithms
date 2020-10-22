def solveNQeensUtil(N, row, pos, result):
    if N == row:
        result.append([p for p in pos])
        return

    for col in range(N):
        foundSafe = True

        for q in range(row):
            if (pos[q][1] == col or
            pos[q][0] - pos[q][1] == row - col or
            pos[q][0] + pos[q][1] == row + col):
                foundSafe = False
                break
        if foundSafe:
            pos[row] = (row, col)
            solveNQeensUtil(N, row + 1, pos, result)

def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    pos = [()]*n
    result = []
    solveNQeensUtil(n, 0, pos, result)
    for r in result:
        print(r)

if __name__ == '__main__':
    solveNQueens(20)