class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        comp = {**{ c : 1 for c in 'qwertyuiop'},
                **{ c : 2 for c in 'asdfghjkl'},
                **{ c : 3 for c in 'zxcvbnm'}}
        
        ans = []
        for word in words:
            tword = word.lower()
            if len(set(list(map(lambda x: comp[x], tword)))) == 1:
                ans.append(word)
        
        return ans
