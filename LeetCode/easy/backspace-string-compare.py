class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        s = ''
        t = ''
        
        """
        "ab#c"
            ^
        """
        step = 0
        for i in range(len(S)-1, -1, -1):
            if S[i] == '#':
                step += 1
            else:
                if step == 0:
                    s += S[i]
                else:
                    step -= 1
        
        step = 0
        for i in range(len(T)-1, -1, -1):
            if T[i] == '#':
                step += 1
            else:
                if step == 0:
                    t += T[i]
                else:
                    step -= 1

        return s == t
