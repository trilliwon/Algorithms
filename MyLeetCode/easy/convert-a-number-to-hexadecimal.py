class Solution(object):
    def toHex(self, num):
        """
        32 bit integer is 8 hex char
        1 char is 4 bit
        
        :type num: int
        :rtype: str
        """
        if num==0:
            return '0'

        m = '0123456789abcdef'
        ans = []
        
        for i in range(8):
            n = num & 15
            c = m[n]
            ans.append(c)
            num >>= 4

        ans = ''.join(ans[::-1])
        return ans.lstrip('0')
