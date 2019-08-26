class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        
        zerosi = set()
        zerosj = set()
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zerosi.add(i)
                    zerosj.add(j)
                    
        for i in range(row):
            for j in range(col):
                if i in zerosi or j in zerosj:
                    matrix[i][j] = 0
