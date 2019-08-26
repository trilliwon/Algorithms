class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return True
        
        for i in range(len(B)):
            newB = ''
            if B[i] == A[0]:
                newB = B[i:] + B[0:i]
                if newB == A:
                    return True
        
        return False
                
