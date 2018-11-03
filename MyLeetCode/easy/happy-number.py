class Solution:
    
    def digitSqrtSum(self, n):
        s = 0
        while n/10 > 0:
            s += (n%10)*(n%10)
            n = int(n/10)
        return s
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        cache = set()
        v = n
        
        while v != 1:
            v = self.digitSqrtSum(v)
            if v in cache:
                return False
            cache.add(v)
            
        return True
