class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        first = 0
        b = bin(N)
        
        # find first 1
        while first < len(b):
            if b[first] == '1':
                break
            else:
                first += 1
        ans = 0
        second = first + 1
        while second < len(b):
            if b[second] == '1':
                ans = max(ans, second - first)
                first = second
                second +=1
            else:
                second += 1
        return ans
