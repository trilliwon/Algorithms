class Solution:

    def getTime(self, bits):
        hour = int(bits[0:4], 2)
        minute = int(bits[4:10], 2)
        
        if minute >= 60 or hour > 11:
            return None

        if minute < 10:
            return str(hour) + ':0' + str(minute)
        
        return str(hour) + ':' + str(minute)

    def backtrack(self, bits, num, start, output):
        """
        :rtype: List[List[int]]
        """
        if num == 0:
            output.append(bits[:])
        else:
            for i in range(start, 10):
                bits[i] = 1
                self.backtrack(bits, num-1, i+1, output)
                bits[i] = 0

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        bits = [0]*10
        output = []
        self.backtrack(bits, num, 0, output)
        output = map(''.join, [map(str, x) for x in output])
        
        ans = []
        
        for time in output:
            time = self.getTime(time)
            if time != None:
                ans.append(time)
        return ans
            
