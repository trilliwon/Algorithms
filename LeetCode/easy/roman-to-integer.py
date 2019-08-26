class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        Roman Numeric
        I - 1
        V - 5
        X - 10
        L - 50
        C - 100
        D - 500
        M - 1000
        
        Rules:
        * If I comes before V or X, subtract 1 eg: IV = 4 and IX = 9
        * If X comes before L or C, subtract 10 eg: XL = 40 and XC = 90
        * If C comes before D or M, subtract 100 eg: CD = 400 and CM = 900
        """
        
        romanNumber = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        rules = { 'IV': 4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM': 900 }
        
        integer = 0
        index = 1
        while index < len(s):
            a = s[index-1]
            b = s[index]            
            ab = a + b

            if ab in rules:
                integer += rules[ab]
                index += 2
            else:
                integer += romanNumber[a]
                index += 1

        # Last 
        if index == len(s):
            integer += romanNumber[s[len(s)-1]]
        return integer

            
            
