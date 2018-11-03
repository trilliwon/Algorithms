class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        answer = []
        isNegativeNumber = num < 0
        num = (-1)*num if isNegativeNumber else num
        
        while num > 0:
            answer.append(str(num % 7))
            num = num // 7
            
        if isNegativeNumber:
            answer.append('-')
        answer.reverse()
        return ''.join(answer)
            
