class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            n = num
            comp = []
            while n != 0:
                comp.append(n%10)
                n //=10
            
            num = sum(comp)
        return num
