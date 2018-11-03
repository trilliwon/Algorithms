class Solution:
    
    def makeCharCountArr(self, s):
        """
        :type s: str
        :rtype: List[(char, int)]
        """
        temp = s[0]
        count = 0
        ls = []
        for x in s:
            if temp == x:
                count += 1
            else:
                ls.append((temp, count))
                temp = x
                count = 1
        ls.append((temp, count))
        return ls
        
    def expressiveWords(self, S, words):
        """
        Complexity
        
        len(S) = a
        len(words) = 
        
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        S = self.makeCharCountArr(S)
        ans = 0
        
        for word in words:
            word = self.makeCharCountArr(word)
            checker = True

            if len(S) == len(word):
                for i in range(len(S)):
                    s_ = S[i]
                    w_ = word[i]
                    if s_[0] == w_[0]:
                        if s_[1] == w_[1]:
                            checker = True
                        elif s_[1] >= 3 and s_[1] >= w_[1]:
                            checker = True
                        else:
                            checker = False
                            break
                    else:
                        checker = False
                        break
                if checker:
                    ans += 1
        
        return ans

