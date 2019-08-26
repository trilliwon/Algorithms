class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        1,2,3
        4,5,6
        7,8,9

        1,4,7
        2,5,8
        3,6,9
        """
        height = len(A)
        width = len(A[0])
        tA = [[0 for _ in range(height)] for _ in range(width)]
        
        for i in range(height):
            for j in range(width):
                tA[j][i] = A[i][j]
        return tA
