class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        paragraph = paragraph.lower()
        banned = [item.lower() for item in banned]

        paragraph = paragraph.replace(",", "")
        paragraph = paragraph.replace(".", "")
        paragraph = paragraph.replace(";", "")
        paragraph = paragraph.replace("?", "")
        paragraph = paragraph.replace("'", "")
        paragraph = paragraph.replace("!", "")
        words = collections.Counter()

        for word in paragraph.split():
            words[word.lower()] += 1
            if word.lower() in banned:
                words[word] = 0

        ans = ("", 0)

        for word, count in words.items():
            if count > ans[1]:
                ans = (word, count)
        return ans[0]
