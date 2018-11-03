class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        ans = 0

        validNumbers = set(['0', '1', '8', '2', '5', '6', '9'])
        shouldContain = set(['2', '5', '6', '9'])

        for n in range(N+1):
            # only contains 0, 1, 8, 2, 5, 6, 9
            # but should contains 2, 5, 6, 9
            s = str(n)
            isValid = True
            for c in s:
                if not (c in validNumbers):
                    isValid = False
            
            if isValid:
                for c in s:
                    if c in shouldContain:
                        ans += 1
                        break
        return ans
