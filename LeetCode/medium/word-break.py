class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if s in wordDict:
            return True
        
        wordDict = set(wordDict)
        cache = dict()

        def wb(word, index):

            if len(word) < index:
                return False

            result = False

            if word[0:index] in wordDict:
                if word[index:] in wordDict:
                    return True
                else:
                    if word[index:] in cache:
                        result = cache[word[index:]]
                    else:
                        result = wb(word[index:], 0)
                        cache[word[index:]] = result

            return result or wb(word, index + 1)

        return wb(s, 1)
