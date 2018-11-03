class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        """
        1 2 3 4
        5 1 2 3
        9 5 1 2
        7 9 5 1
        
        h, w
        h-1,
        (2, 0)  (1, 0)  (0, 0)  (0, 1)  (0, 2)
        (3, 1)  (2, 1)  (1, 1)  (1, 2)  (1, 3)
                (3, 2)  (2, 2)  (2, 3)
                        (3, 3)  
        """
        h = len(matrix)
        w = len(matrix[0])
        
        # diagonal
        l = max(w, h)
        for k in range(l):
            # right
            checker = set()
            for i in range(h):
                j = i + k
                if i < h and j < w:
                    checker.add(matrix[i][j])
                if len(checker) > 1:
                    return False
            # left
            checker = set()
            for i in range(h):
                j = i
                i = i + k
                if i < h and j < w:
                    checker.add(matrix[i][j])

                if len(checker) > 1:
                    return False

        return True
            
        
