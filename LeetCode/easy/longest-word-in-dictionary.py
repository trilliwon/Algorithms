class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        words.sort()
        words.sort(key=len, reverse=True)
        wordsDic = collections.Counter(words)

        for word in words:
            if all(word[0:i] in wordsDic for i in range(1, len(word))):
                return word
        return ''
