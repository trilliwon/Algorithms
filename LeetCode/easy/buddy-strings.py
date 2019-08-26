class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        if len(A) < 2:
            return False
        
        numA = collections.Counter(A)
        
        if numA != collections.Counter(B):
            return False
        
        diff = 0
        hasDup = False
        
        for a, b in zip(A, B):
            if numA[a] > 1:
                hasDup = True
            if a != b:
                diff += 1

        return diff == 2 or (hasDup and A == B)
