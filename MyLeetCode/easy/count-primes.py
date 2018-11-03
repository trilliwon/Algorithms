class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        s = [1] * n     # init
        s[0] = s[1] = 0 # set 0, 1 with zero
        for i in range(2, int(n ** 0.5) + 1): # 2 to root(n) + 1
            if s[i] == 1:
                s[i * i:n:i] = [0] * len(s[i * i:n:i]) # set as 0 all the elements by step i
        return sum(s)
