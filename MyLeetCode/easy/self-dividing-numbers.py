class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        ans = []
        
        # loop from left to right
        for num in range(left, right+1):
            n = num # temp num
            t = [] # temp arr
            while n > 0:
                digit = n % 10
                t.append(digit != 0 and num % digit == 0)
                n //= 10
            if all(t):
                ans.append(num)
        return ans
