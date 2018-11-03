class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        max n : 4,294,967,296 - 10 digits
        1. how many digits, n = 250 - 9 - 90*2 = 61
        2. what is the number, n = 100+61/3
        3. which digit is we want to find
        """
        if n in range(1, 10):
            return n

        ans = 0
        for digits in range(1, 11):
            before = 9*(10**(digits-1))*digits
            if n < before:
                number = 10**(digits-1) + n // digits
                ans = str(number - 1)[digits-1] if n % digits == 0 else str(number)[n%digits-1]
                break
            n -= before
        return int(ans)
