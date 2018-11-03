class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        min_str_len = min([len(s) for s in strs])
        output = []
        
        for i in range(min_str_len):
            c = strs[0][i]
            flag = True
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    flag = False
                    break
            if flag:
                output.append(c)
            else:
                break
        
        return ''.join(output)
        
