class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        def perm(index, output, s):
            if index < len(s):
                perm(index+1, output, s)
                if s[index].isalpha():
                    s[index] = s[index].upper() if s[index].islower() else s[index].lower()
                    perm(index+1, output, s)
            output.add(''.join(s))
        output = set()
        S = S.lower()
        output.add(S.lower())
        perm(0, output, list(S))

        return list(output)
