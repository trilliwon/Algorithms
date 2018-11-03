class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)

        def reverse(s, lower, upper):
            index = 0
            for i in range(lower, (upper+lower)//2):
                s[i], s[upper - index - 1] = s[upper - index - 1], s[i]
                index += 1

        flag = True
        for index in range(0, len(s), k):
            if flag:
                if index + k <= len(s):
                    print(''.join(s[index:index+k]), index, index+k)
                    reverse(s, index, index+k)
                    flag = False
                elif index + k > len(s):
                        reverse(s, index, len(s))
            else:
                flag = True
        return ''.join(s)
