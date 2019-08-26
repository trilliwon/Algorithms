class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        [2  ,3  ,4],
        [5  ,6  ,7],
        [8  ,9  ,10]
        [11 ,12 ,13]
        [14 ,15 ,16]
        """
        
        pos = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        h = len(M)
        w = len(M[0])
        rM = [ [0]*w for i in [0]*h]

        for i in range(h):
            for j in range(w):
                con = []
                con.append(M[i][j])
                for k in pos:
                    nx = i + k[0]
                    ny = j + k[1]
                    if nx < h and nx >= 0 and ny < w and ny >= 0:
                        con.append(M[nx][ny])
                rM[i][j] = int(sum(con)/len(con))
        return rM
